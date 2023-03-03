pip install -U Selenium
pip install behave
pip install html-formatter
pip install webdriver-manager
pip install browser

#run test
behave -f behave_html_formatter:HTMLFormatter -o test-report.html --tags=tinta
