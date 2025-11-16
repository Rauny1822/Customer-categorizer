import sys
import os
from dotenv import load_dotenv

# Load environment
load_dotenv('.env', override=True)
os.environ['PYTHONPATH'] = '.'

import traceback
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def main():
    try:
        from src.pipeline.train_pipeline import TrainPipeline
        print('='*60)
        print('Starting training pipeline...')
        print('='*60)
        pipeline = TrainPipeline()
        pipeline.run_pipeline()
        print('='*60)
        print('TRAINING PIPELINE COMPLETED SUCCESSFULLY')
        print('='*60)
    except Exception as e:
        print('='*60)
        print('EXCEPTION during training pipeline:')
        print('='*60)
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
