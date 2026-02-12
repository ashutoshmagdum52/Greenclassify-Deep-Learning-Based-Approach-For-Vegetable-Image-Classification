# GreenClassify - Vegetable Image Classification Web Application

## Project Overview
A professional web application for classifying vegetable images using machine learning with a beautiful green-themed interface.

## 🎯 Model Capabilities

The trained model can classify **15 different vegetables**:

1. Bean 🫘
2. Bitter Gourd 🥒
3. Bottle Gourd 🫙
4. Brinjal (Eggplant) 🍆
5. Broccoli 🥦
6. Cabbage 🥬
7. Capsicum (Bell Pepper) 🫑
8. Carrot 🥕
9. Cauliflower 🥦
10. Cucumber 🥒
11. Papaya 🍈
12. Potato 🥔
13. Pumpkin 🎃
14. Radish 🌱
15. Tomato 🍅

## Files Created/Updated

### HTML Templates (in `templates/` folder):
1. **index.html** - Home page with hero section and navigation
2. **about.html** - About page with company information
3. **contact.html** - Contact page with contact details
4. **prediction.html** - Main prediction page with upload form and results display
5. **logout.html** - Logout/Thank you page

### CSS (in `static/` folder):
1. **style.css** - Complete styling with green theme, responsive design, and animations

### Python Application:
1. **app.py** - Flask application with:
   - Correct model loading (vegetable_model.h5)
   - All 15 vegetable class labels
   - Error handling for predictions
   - Image handling for display in results
   - All necessary routes

## Features Implemented

✅ Professional green color theme (#2C5F2D, #A8E6CF)
✅ Responsive navigation menu
✅ Hero section on home page
✅ File upload with visual feedback
✅ Result display with uploaded image preview
✅ Animated vegetable characters (emojis)
✅ Fully responsive design
✅ About and Contact pages
✅ Footer on all pages
✅ Error handling for unknown classes

## How to Run the Application

### Prerequisites:
- Python 3.x
- Flask
- TensorFlow/Keras
- NumPy

### Installation Steps:

1. Install required packages:
```bash
pip install flask tensorflow keras numpy pandas
```

2. Make sure your model file is present:
   - File should be: `vegetable_model.h5`
   - Located in the project root directory

3. Navigate to project folder:
```bash
cd "G:\AM\swayam course\vegetables image classification"
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and go to:
```
http://127.0.0.1:5000/
```

## Application Structure

```
vegetables image classification/
├── app.py                    # Main Flask application
├── vegetable_model.h5        # Trained ML model (15 classes)
├── uploads/                  # Temporary uploaded images
├── templates/
│   ├── index.html           # Home page
│   ├── about.html           # About page
│   ├── contact.html         # Contact page
│   ├── prediction.html      # Prediction page
│   └── logout.html          # Logout page
└── static/
    ├── style.css            # Main stylesheet
    └── uploads/             # Images for display
```

## Key Features & Fixes

1. ✅ **All 15 vegetable classes supported** - No more KeyError!
2. ✅ **Error handling** - Uses `.get()` method to prevent crashes
3. ✅ **Professional design** - Green theme matching screenshots
4. ✅ **Image preview** - Shows uploaded image in circular frame
5. ✅ **Responsive layout** - Works on mobile and desktop
6. ✅ **Complete navigation** - Home, About, Contact, Prediction pages

## Pages Available

1. **Home (/)** - Landing page with hero section
2. **About (/about)** - Information about GreenClassify
3. **Contact (/contact)** - Contact information
4. **Prediction (/prediction)** - Upload and classify vegetables
5. **Logout (/logout.html)** - Thank you page

## Usage Instructions

### Basic Usage:
1. Navigate to the Prediction page
2. Click "Choose File" to select a vegetable image
3. Click "Submit" to classify
4. View the result with the uploaded image preview
5. Upload another image or navigate to other pages

### Supported Image Formats:
- JPG / JPEG
- PNG
- WEBP
- Other common image formats

### Best Results:
- Clear, well-lit images
- Single vegetable in frame
- Close-up shots preferred
- Good contrast against background

## Troubleshooting

### Problem: "ModuleNotFoundError"
**Solution:**
```bash
pip install flask tensorflow keras numpy pandas
```

### Problem: "Model file not found"
**Solution:**
- Ensure `vegetable_model.h5` exists in project root
- Check the filename is exactly correct (case-sensitive)

### Problem: "KeyError: np.int64(X)"
**Solution:**
- This has been fixed! The dictionary now includes all 15 classes (0-14)
- If you still see this, check that you're using the updated `app.py`

### Problem: "Images don't display"
**Solution:**
- Check that `static/uploads/` folder exists
- Clear browser cache (Ctrl+F5)
- Verify file permissions

### Problem: "Port already in use"
**Solution:**
- Stop the previous instance (Ctrl+C)
- Or change the port:
```python
# In app.py, last line:
app.run(debug=True, port=5001)
```

## Technical Details

### Model Specifications:
- Input size: 150x150 pixels
- Architecture: CNN (Convolutional Neural Network)
- Number of classes: 15
- Output: Class probabilities (0-14)

### How It Works:
1. User uploads image
2. Image resized to 150x150
3. Image converted to array
4. Model predicts class (0-14)
5. Class mapped to vegetable name
6. Result displayed with image preview

## Customization Options

You can easily customize:
- **Colors**: Edit `style.css` (search for #2C5F2D and #A8E6CF)
- **Logo**: Change "GreenClassify.com" in header
- **Contact info**: Edit `contact.html`
- **About text**: Edit `about.html`
- **Vegetable emojis**: Change emojis in `prediction.html`
- **Class names**: Modify the `op` dictionary in `app.py`

## Important Files

### Core Application Files:
- `app.py` - Main Flask application with all routes and logic
- `vegetable_model.h5` - Pre-trained TensorFlow/Keras model

### Template Files:
- `templates/*.html` - All HTML pages

### Static Files:
- `static/style.css` - All styling
- `static/uploads/` - Uploaded images for display

### Documentation:
- `README.md` - This file
- `QUICK_START.md` - Quick start guide
- `ERROR_KEYERROR_FIXED.md` - KeyError fix documentation
- `ISSUES_FIXED.md` - All issues resolved
- `FIXES_VERIFICATION.md` - Testing guide

## Development Notes

### Error Handling:
The application includes robust error handling:
```python
result = op.get(pred, f'Unknown (Class {pred})')
```
This prevents crashes if the model predicts an unexpected class.

### Security Considerations:
- File uploads are validated
- Images stored in designated folders
- Form uses POST method
- CSRF protection recommended for production

### Future Enhancements:
- Add user authentication
- Save classification history
- Batch image processing
- Confidence scores display
- Export results to CSV
- Multi-language support

## Credits

- **Framework**: Flask
- **ML Library**: TensorFlow/Keras
- **Design**: Custom green theme
- **Model**: Vegetable classification CNN

## License

This project is for educational purposes.

---

## Quick Commands

### Start Application:
```bash
python app.py
```

### Access Application:
```
http://127.0.0.1:5000/
```

### Stop Application:
```
Ctrl+C in terminal
```

### Clear Uploads:
```bash
# Windows
del /q "uploads\*.*"
del /q "static\uploads\*.*"

# Linux/Mac
rm -f uploads/*
rm -f static/uploads/*
```

---

## Summary

✅ **15 vegetables** can be classified
✅ **Professional design** with green theme
✅ **Error-free** with proper handling
✅ **Responsive** design for all devices
✅ **Easy to use** interface
✅ **Well documented** with guides

**Ready to classify vegetables! Upload an image and try it out! 🥕🥒🍅**
