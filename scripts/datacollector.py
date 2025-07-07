import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
import os
from tqdm import tqdm

def scrape_cricinfo_innings(url):
    """
    Scrape innings data from ESPN Cricinfo and save to CSV
    """
    
    # Headers to mimic a real browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # Make the request
        print("Fetching data from ESPN Cricinfo...")
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # Parse the HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the innings table
        # Look for table with class that contains innings data
        tables = soup.find_all('table')
        
        innings_data = []
        headers = []
        
        # Look for the main data table
        for table in tables:
            # Check if this table contains innings data
            th_elements = table.find_all('th')  # type: ignore
            if th_elements and any('Inn' in th.get_text() or 'Score' in th.get_text() 
                                  for th in th_elements):
                
                # Extract headers
                headers_row = table.find('tr')  # type: ignore
                if headers_row:
                    headers = [th.get_text().strip() for th in headers_row.find_all(['th', 'td'])]  # type: ignore
                    
                    # Extract data rows
                    rows = table.find_all('tr')[1:]  # Skip header row  # type: ignore
                    
                    for row in rows:
                        cells = row.find_all(['td', 'th'])  # type: ignore
                        if cells:
                            row_data = []
                            for cell in cells:
                                # Clean the cell text
                                text = cell.get_text().strip()
                                # Remove extra whitespace and newlines
                                text = re.sub(r'\s+', ' ', text)
                                row_data.append(text)
                            
                            if len(row_data) == len(headers):
                                innings_data.append(row_data)
        
        # If no specific table found, try to find all tables and let user choose
        if not innings_data:
            print("Searching for all tables...")
            all_tables_data = []
            
            for i, table in enumerate(tables):
                table_data = []
                rows = table.find_all('tr')  # type: ignore
                
                if len(rows) > 1:  # Must have at least header and one data row
                    for row in rows:
                        cells = row.find_all(['td', 'th'])  # type: ignore
                        if cells:
                            row_data = [cell.get_text().strip() for cell in cells]
                            table_data.append(row_data)
                    
                    if table_data:
                        all_tables_data.append((i, table_data))
            
            # Use the largest table (most likely to be the main data table)
            if all_tables_data:
                largest_table = max(all_tables_data, key=lambda x: len(x[1]))
                table_data = largest_table[1]
                
                if table_data:
                    headers = table_data[0]
                    innings_data = table_data[1:]
        
        # Create DataFrame
        if innings_data and headers:
            # Ensure headers and data have matching lengths
            if len(headers) != len(innings_data[0]) if innings_data else 0:
                print(f"Warning: Headers length ({len(headers)}) doesn't match data length ({len(innings_data[0]) if innings_data else 0})")
                # Use the data length to create headers if needed
                if innings_data:
                    data_length = len(innings_data[0])
                    if len(headers) < data_length:
                        headers.extend([f"Column_{i+1}" for i in range(len(headers), data_length)])
                    else:
                        headers = headers[:data_length]
            
            # Clean headers
            headers = [str(h).replace('\n', ' ').replace('\r', ' ').strip() for h in headers]
            
            # Add missing column names
            if len(headers) >= 12 and not headers[11]:  # Column 12 (index 11) is empty
                headers[11] = 'format'
            
            df = pd.DataFrame(innings_data, columns=headers)  # type: ignore
            
            # Clean column names
            df.columns = [col.replace('\n', ' ').replace('\r', ' ').strip() for col in df.columns]
            
            # Create data directory path and save to CSV
            data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
            
            # Ensure data directory exists
            os.makedirs(data_dir, exist_ok=True)
            
            filename = os.path.join(data_dir, 'cricinfo_innings_data_final.csv')
            df.to_csv(filename, index=False, encoding='utf-8')
            
            print(f"Data successfully saved to {filename}")
            print(f"Number of rows: {len(df)}")
            print(f"Columns: {list(df.columns)}")
            print("\nFirst few rows:")
            print(df.head())
            
            return df
            
        else:
            print("No innings data found. The page structure might be different.")
            
            # Save page content for debugging in data folder
            data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
            os.makedirs(data_dir, exist_ok=True)
            debug_file = os.path.join(data_dir, 'debug_page.html')
            
            with open(debug_file, 'w', encoding='utf-8') as f:
                f.write(response.text)
            print(f"Page content saved to {debug_file} for inspection")
            
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None
    except Exception as e:
        print(f"Error processing the data: {e}")
        return None

def main():
    url = "https://stats.espncricinfo.com/ci/engine/team/1.html?class=11;template=results;type=team;view=innings"
    
    print("ESPN Cricinfo Innings Data Scraper")
    print("=" * 40)
    
    # Add a small delay to be respectful to the server
    time.sleep(1)
    
    df = scrape_cricinfo_innings(url)
    
    if df is not None:
        print("\nScraping completed successfully!")
        
        # Display some basic statistics
        print(f"\nDataset shape: {df.shape}")
        print(f"Column names: {', '.join(df.columns)}")
        
        # Ask if user wants to see more details
        try:
            show_details = input("\nWould you like to see the full dataset? (y/n): ").lower()
            if show_details == 'y':
                print("\nFull dataset:")
                print(df.to_string())
        except:
            pass
    else:
        print("\nScraping failed. Please check the URL and try again.")
        print("The page might require JavaScript or have anti-bot protection.")

if __name__ == "__main__":
    main()