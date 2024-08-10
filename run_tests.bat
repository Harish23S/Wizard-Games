@echo off

:: Get the current date and time in the format YYYYMMDD_HHMMSS
:: Replace spaces with zeros to avoid issues in the filename
set timestamp=%date:~10,4%%date:~4,2%%date:~7,2%_%time:~0,2%%time:~3,2%%time:~6,2%
set timestamp=%timestamp: =0%

:: Define the report file name
set report_file=tests\reports\report_%timestamp%.txt

:: Run Behave and save the output to the timestamped report file
behave --format=plain --outfile=%report_file%
pause
