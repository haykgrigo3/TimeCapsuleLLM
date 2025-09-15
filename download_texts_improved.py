"""download_texts_improved_clean.py


# Made for London v0

# What it does:
    - You provide a text file (e.g. ids.txt) with one Archive.org item ID per line.
    - The script loops over that list and tries to download the text files for each ID.

Usage:
    # set env var (recommended)
    export ARCHIVE_API_KEY="your_api_key_here"
    python download_texts_improved_clean.py --ids ids.txt --outdir ./texts --concurrency 8

    # or pass API key directly (less secure)
    python download_texts_improved_clean.py --ids ids.txt --outdir ./texts --api-key YOUR_KEY
"""

from __future__ import annotations
import argparse
import concurrent.futures
import os
import sys

import time

import logging
from pathlib import Path
from typing import Optional
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

VERSION = "0"

DEFAULT_CONCURRENCY = 4

DEFAULT_TIMEOUT = 30  # seconds


def setup_logger(verbose: bool = False) -> logging.Logger:
    level = logging.DEBUG if verbose else logging.INFO
    logger = logging.getLogger("download_texts")
   
   
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s", "%Y-%m-%d %H:%M:%S")
        
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(level)
    return logger


def requests_session_with_retries(
    total_retries: int = 5,
    
    backoff_factor: float = 0.5,
    status_forcelist=(429, 500, 502, 503, 504),
):
    session = requests.Session()
    retries = Retry(
        total=total_retries,
        read=total_retries,
        connect=total_retries,
        
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
        
        allowed_methods=frozenset(["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS"]),
    )
    adapter = HTTPAdapter(max_retries=retries)
    
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    session.headers.update(
        {
            "User-Agent": f"TXTDownloader/{VERSION} (+https://github.com/haykgrigo3/TimeCapsuleLLM)"
        
        }
    )
    
    return session


def download_text(
    
    
    item_id: str,
    outdir: Path,
    session: requests.Session,
    api_key: Optional[str],
    logger: logging.Logger,
   
    timeout: int = DEFAULT_TIMEOUT,
) -> tuple[str, bool, str]:
    """Download a text for a given item id. Returns (item_id, success, message)."""

    candidates = [
        f"{item_id}_djvu.txt",
        f"{item_id}.txt",
       
        f"{item_id}_ocr.txt",
        f"{item_id}-text.txt",
    ]
    outdir.mkdir(parents=True, exist_ok=True)
    for filename in candidates:
        url = f"https://archive.org/download/{item_id}/{filename}"
        
        dest = outdir / filename
        if dest.exists() and dest.stat().st_size > 0:
            logger.debug(f"Skipping {item_id} — {filename} already exists.")
            return (item_id, True, f"skipped {filename}")
        try:
            headers = {}
           
            if api_key:
                headers["Authorization"] = f"Bearer {api_key}"
            logger.debug(f"Trying URL: {url}")
            resp = session.get(url, headers=headers, timeout=timeout, stream=True)
            if resp.status_code == 200 and resp.headers.get("Content-Type", "").lower().startswith("text"):
                with open(dest, "wb") as f:
                  
                    for chunk in resp.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                logger.info(f"Downloaded {item_id} -> {dest.name}")
                return (item_id, True, f"downloaded {filename}")
            else:
                logger.debug(
                    f"Not found or non-text: {url} (status {resp.status_code}, type {resp.headers.get('Content-Type')})"
                )
      
        except requests.RequestException as e:
          
            logger.warning(f"Error fetching {url}: {e}")
    return (item_id, False, "no candidate file found")


def load_ids_from_file(path: Path) -> list[str]:
    if not path.exists():
   
        raise FileNotFoundError(f"IDs file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
     
        ids = [line.strip() for line in f if line.strip() and not line.strip().startswith("#")]
    return ids


def parse_args(argv=None):
    p = argparse.ArgumentParser(
    
        description="Download plain text files for a list of Internet Archive item IDs (safe for GitHub).",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--ids", "-i", type=Path, required=True, help="Path to a newline-separated file containing item ids (one per line).")
    p.add_argument("--outdir", "-o", type=Path, default=Path("./texts"), help="Directory to write downloaded text files.")
   
   
    p.add_argument("--api-key", "-k", type=str, default=None, help="API key (not recommended on CLI; use ARCHIVE_API_KEY env var).")
    p.add_argument("--concurrency", "-c", type=int, default=DEFAULT_CONCURRENCY, help="Number of worker threads for downloads.")
    p.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT, help="HTTP request timeout in seconds.")
    
    p.add_argument("--verbose", "-v", action="store_true", help="Enable verbose logging (debug).")
    p.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    return p.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    logger = setup_logger(args.verbose)
   
    api_key = args.api_key or os.environ.get("ARCHIVE_API_KEY") or os.environ.get("IA_API_KEY")
    if not api_key:
        logger.warning("No API key found in --api-key or environment variables. Script will still attempt public downloads but some endpoints may require a key.")
    try:
      
        ids = load_ids_from_file(args.ids)
    except Exception as e:
      
        logger.error(f"Failed to load ids: {e}")
        sys.exit(2)

    logger.info(f"Starting download of {len(ids)} items with concurrency={args.concurrency}")
   
    session = requests_session_with_retries()
    results = []
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.concurrency)) as ex:
      
        futures = {ex.submit(download_text, item_id, args.outdir, session, api_key, logger, args.timeout): item_id for item_id in ids}
        for fut in concurrent.futures.as_completed(futures):
            item = futures[fut]
            try:
                res = fut.result()
                results.append(res)
            except Exception as e:
                logger.exception(f"Unhandled error downloading {item}: {e}")
                results.append((item, False, f"exception: {e}"))

    elapsed = time.time() - start_time
    success_count = sum(1 for _, ok, _ in results if ok)
    fail_count = len(results) - success_count
    logger.info(f"Done — {success_count} succeeded, {fail_count} failed. Elapsed: {elapsed:.1f}s")

    report_path = args.outdir / "download_report.csv"
    try:
        with open(report_path, "w", encoding="utf-8") as f:
            f.write("item_id,success,message\n")
            for item_id, ok, msg in results:
                f.write(f"\"{item_id}\",{int(ok)},\"{msg.replace('\"','\"\"')}\"\n")
        logger.info(f"Wrote report: {report_path}")
   
    except Exception as e:
        logger.warning(f"Could not write report: {e}")


if __name__ == "__main__":
  
    main()
