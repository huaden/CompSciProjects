from flask import Flask, render_template, url_for, jsonify, request, Response
import requests
from barcodeGetter import getBarcode, getProductInfo
import cv2






app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/barcode_info', methods=['GET', 'POST'])
def barcode_info():
    barcodeNum = getBarcode()
    productInfo = getProductInfo(barcodeNum)
    print(productInfo)

    return render_template('foodInfo.html', product=productInfo, barcode=barcodeNum)


if __name__ == "__main__":
    app.run(port=5001, debug=True)