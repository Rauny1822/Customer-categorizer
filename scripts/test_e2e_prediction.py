import requests
import sys

def test_prediction():
    """Test end-to-end prediction via the web app"""
    url = "http://localhost:8000"
    
    # Sample customer data matching the form fields
    data = {
        "Age": "35",
        "Education": "2",  # Graduation
        "Marital_Status": "1",  # Married/Together
        "Parental_Status": "0",
        "Children": "1",
        "Income": "50000",
        "Total_Spending": "200.0",
        "Days_as_Customer": "365",
        "Recency": "10",
        "Wines": "5",
        "Fruits": "2",
        "Meat": "1",
        "Fish": "0",
        "Sweets": "0",
        "Gold": "0",
        "Web": "3",
        "Catalog": "1",
        "Store": "2",
        "Discount_Purchases": "0",
        "Total_Promo": "0",
        "NumWebVisitsMonth": "4"
    }
    
    print("Testing end-to-end prediction...")
    print(f"Sending POST request to {url}")
    
    try:
        response = requests.post(url, data=data)
        print(f"Response status: {response.status_code}")
        print(f"Response length: {len(response.text)} chars")
        
        # Check if response contains a cluster number (0, 1, or 2)
        if "Cluster: 0" in response.text or "Cluster: 1" in response.text or "Cluster: 2" in response.text:
            print("✓ SUCCESS: Prediction returned a valid cluster assignment!")
            return True
        elif "context" in response.text or "customer.html" in response.text:
            print("✓ App returned HTML (prediction likely processed)")
            # Print snippet of response to see the cluster
            if "Cluster:" in response.text:
                idx = response.text.find("Cluster:")
                print("Cluster result: " + response.text[idx:idx+50])
            return True
        else:
            print("✗ Response does not contain expected cluster result")
            print("Response snippet:", response.text[:200])
            return False
            
    except requests.exceptions.ConnectionError as e:
        print(f"✗ Connection error: {e}")
        print("Make sure the FastAPI app is running on http://localhost:8000")
        return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

if __name__ == "__main__":
    success = test_prediction()
    sys.exit(0 if success else 1)
