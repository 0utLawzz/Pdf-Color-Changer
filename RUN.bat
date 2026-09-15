@echo off
setlocal
title PDF Color Changer

echo ==========================================
echo       PDF COLOR CHANGER - BRANDEX
echo ==========================================
echo.

where python >nul 2>nul
if errorlevel 1 (
    echo Python was not found.
    echo Please install Python and try again.
    echo.
    pause
    exit /b 1
)

python -c "import fitz" >nul 2>nul
if errorlevel 1 (
    echo PyMuPDF is not installed. Installing it now...
    echo.
    python -m pip install pymupdf
    if errorlevel 1 (
        echo.
        echo Installation failed.
        pause
        exit /b 1
    )
)

if not exist "%~dp0PDF_Color_Changer.py" (
    echo.
    echo ERROR: PDF_Color_Changer.py was not found.
    echo Keep this BAT file in the same folder as PDF_Color_Changer.py
    echo.
    pause
    exit /b 1
)

echo Starting PDF Color Changer...
echo.
python "%~dp0PDF_Color_Changer.py"

if errorlevel 1 (
    echo.
    echo The program closed with an error.
    pause
)

endlocal
