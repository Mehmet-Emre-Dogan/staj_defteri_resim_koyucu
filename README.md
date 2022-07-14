# staj_defteri_resim_koyucu
 Add your photo automagically to the "staj defteri"

 # Setup

 ## Python
 - Download source code
 - Install Python
    - https://www.python.org/downloads/
    - Make sure you add python to `path`
 - Extract the source code to a `folder`
 - Install the libraries
    - Open command prompt in that `folder`
    - Run prompt `python -m pip install -r requirements.txt`

 ## Exe
  - Download the latest version from the `releases`
  - Extract the files to a `folder`

 # Usage
  - Go the the `folder` where app is
  - Delete `photo.jpg`
  - Crop your photo to `310x380` px
  - Rename your photo to `photo.jpg`
  - Run the app
  - Your photo embedded pdf is created: `document-output.pdf`

  # Troubleshooting
  ## Access/Permission Denied Error
  - This occurs when a file that going to be written is opened by user.
    - Close `document-output.pdf`, `temp_watermark.pdf` etc.
  ## My photo is misaligned
  - Make sure to crop your photo to `310x380` px
  - You may also play with the coordinates in lines 8&9 if you are using .py version
  ## Other Errors
  - Create a well documented issue (with screenshots etc.). I will try to help you.