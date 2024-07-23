from pyzbar import pyzbar
import cv2
import requests
from flask import jsonify


def getBarcode():
    # starts video stream
    vs = cv2.VideoCapture(0)
    found = set()

    while True:
        # every frame is broken down/resized

        ret, frame = vs.read()
        if not ret:
            print("Failed to retrieve frame from the video stream.")
        #    break
        # decode frame to have list of frames
        barcodes = pyzbar.decode(frame)
        for barcode in barcodes:
            barcodeData = barcode.data.decode("utf-8")
            found.add(barcodeData)

        # shows camera window to user and waits for key
        #cv2.imshow('frame', frame)
        key = cv2.waitKey(1) & 0xFF
            # 'q' closes the window or when a barcode is found
        if key == ord('q') or len(found) > 0:
                break
        

    # closes all windows, and ends video stream
    cv2.destroyAllWindows()
    vs.release()
    
    return list(found)
#def BarcodeReader(image):

def getProductInfo(barcode):
    URL = "https://world.openfoodfacts.net/api/v2/product/"
    url = f'{URL}{barcode}.json'
    response = requests.get(url)
    if (response.status_code != 200):
        return jsonify({"error": "failed to get data"}), 500
    
    data = response.json() #gets the data and can now access based on data format

    product = data['product']
    nutriments = product.get('nutriments', {})
    product_info = {
        'name': product.get('product_name', 'N/A'),
        'allergens': product.get('allergens_from_ingredients', 'N/A'),
        'serving_size': product.get('serving_size', 'N/A'),
        'ingredients': product.get('ingredients_text', 'N/A'),
        
        'fat': nutriments.get('fat', 'N/A'),
        'fat_unit': nutriments.get('fat_unit', ''),
        'cholesterol': nutriments.get('cholesterol', 'N/A'),
        'cholesterol_unit': nutriments.get('cholesterol_unit', ''),
        'sodium': nutriments.get('sodium', 'N/A'),
        'sodium_unit': nutriments.get('sodium_unit', ''),
        'carbohydrates': nutriments.get('carbohydrates', 'N/A'),
        'carbohydrates_unit': nutriments.get('carbohydrates_unit', ''),
        'sugars': nutriments.get('sugars', 'N/A'),
        'sugars_unit': nutriments.get('sugars_unit', ''),
        'proteins': nutriments.get('proteins', 'N/A'),
        'proteins_unit': nutriments.get('proteins_unit', ''),
        'status_verbose' : data.get('status_verbose')
    }
    return product_info


#x = getBarcode()
#print(x)