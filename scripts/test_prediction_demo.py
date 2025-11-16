from dotenv import load_dotenv
import os

# Load .env but then unset AWS vars to force demo mode
load_dotenv('.env', override=True)
os.environ.pop('AWS_ACCESS_KEY_ID', None)
os.environ.pop('AWS_SECRET_ACCESS_KEY', None)
os.environ.pop('AWS_REGION', None)

from src.pipeline.prediction_pipeline import PredictionPipeline

def main():
    # sample input matching prediction schema columns
    sample_input = [30, 2, 1, 0, 1, 50000, 200.0, 365, 10, 5, 2, 1, 0, 0, 0, 3, 1, 2, 0, 0, 4]
    pp = PredictionPipeline()
    pred = pp.run_pipeline(sample_input)
    print('PREDICTION', pred)

if __name__ == '__main__':
    main()
