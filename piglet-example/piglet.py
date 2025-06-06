#!/usr/bin/env python3
"""
Entry point for the console application.
"""
import sys
import os
import argparse
import logging


def setup_logging():
    """Configure logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )
    return logging.getLogger(__name__)


def main():
    """
    Main entry point for the application.

    Returns:
        int: Exit code (0 for success, non-zero for errors)
    """
    try:
        logger = setup_logging()
        logger.debug("Application started")

        # Set up argument parser
        parser = argparse.ArgumentParser(description="Process a text file.")
        parser.add_argument("file_name", help="The path to the text file to process")
        
        # Parse arguments
        args = parser.parse_args()
        
        # Validate file existence
        if not os.path.isfile(args.file_name):
            logger.error(f"Error: The file '{args.file_name}' does not exist or is not accessible.")
            return 2
        
        # Log the file that will be processed
        logger.info(f"Processing file: {args.file_name}")

        # Main application logic would go here
        
        logger.debug("Application completed successfully")
        return 0
    except Exception as e:
        # If logger is not defined (e.g., setup_logging failed), use root logger
        try:
            logger.error(f"An error occurred: {e}", exc_info=True)
        except UnboundLocalError:
            # Fallback to root logger if logger is not defined
            logging.error(f"An error occurred during application startup: {e}", exc_info=True)
        
        return 1


if __name__ == "__main__":
    sys.exit(main())