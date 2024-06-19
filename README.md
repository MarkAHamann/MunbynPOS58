# Printer Program for Munbyn POS-58 (Windows)

The Munbyn POS-58 receipt printer is a small receipt thermal printer.

It is about $50 on amazon.com.

My usage is for printing radio communications in emergency and drill
situations. Communication can come in by radio and I can enter it
as I hear it into a program like notepad or winlink.

Then if I want to print it out, I can either:
* drag text and drop it into this program
* copy to the clipboard and right click in this program

In either case, it will print the text to the POS-58 printer.

## Usage
```
> pip install -r requirements
> pyinstaller -F .\recprn.py -w --additional-hooks-dir=.
```

Then copy .\recprn\recprn.exe to a useful place to launch the app.

To use, drag text from one app to the body of recprn, or copy it to the
clipboard and right click in the recprn.

You can select the font size from 8 to 14.

## Future Enhancements

* Printer Picker (drodown)
* Accept file, detect format:
    - if an ICS-213 (Winlink format), print the relevant data
    - if just text, print the file
    - if ???, do ???
