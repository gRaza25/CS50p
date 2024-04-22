# YouTube Channel Data Extractor

#### Video Demo: [https://www.youtube.com/watch?v=12VBwU6gkYA]

## Description:
The YouTube Channel Data Extractor is a Python script designed to streamline the process of fetching detailed information about YouTube channels and their videos using the YouTube Data API. This script serves as a powerful tool for data analysts, content creators, and YouTube enthusiasts alike, enabling them to gain insights into channel metrics and video performance effortlessly.

### Features:

1. **Channel Information Retrieval**:
    - Fetches essential details about a specified YouTube channel, including its name, subscriber count, and total number of videos.
    - Utilizes the YouTube Data API to ensure accurate and up-to-date information retrieval.

2. **Video Data Extraction**:
    - Retrieves a comprehensive list of videos associated with the specified channel, along with crucial metrics such as titles, release dates, and view counts.
    - Handles pagination seamlessly to ensure that all videos from the channel's playlist are captured.

3. **User-Friendly Interface**:
    - Offers a straightforward command-line interface (CLI) for users to input the desired YouTube channel ID and initiate the data extraction process effortlessly.
    - Provides clear prompts and instructions for smooth interaction, enhancing user experience.

### Implementation:

The project comprises two primary Python files:

- **main.py**: This file serves as the core script, orchestrating the interaction with the YouTube Data API to retrieve channel and video data based on user input.
- **test.py**: Contains a suite of unit tests developed using pytest to validate the functionality of key functions responsible for fetching channel details, video IDs, and video lists.

### Libraries and Dependencies:

To facilitate seamless interaction with the YouTube Data API and enhance data presentation, the project leverages the following libraries:

- **google-api-python-client**: Enables communication with the YouTube Data API, empowering the script to fetch channel and video data efficiently.
- **tabulate**: Facilitates the formatting of retrieved data into visually appealing tables, enhancing readability for users.

### Usage:

1. **Installation**:
    - Ensure that Python and the necessary dependencies (`google-api-python-client`, `tabulate`) are installed in your environment.

2. **Execution**:
    - Run the `main.py` script and follow the prompts to input the YouTube channel ID.
    - Upon execution, the script will fetch and display the requested channel details and associated video information.

### Testing:

Comprehensive unit tests have been implemented using pytest to validate the functionality of critical functions within the project. These tests ensure the reliability and accuracy of data retrieval processes, contributing to the overall robustness of the script.

### Contributions and Feedback:

Contributions to this project are highly encouraged! Whether it's addressing bugs, implementing new features, or enhancing existing functionality, your contributions can make a significant difference. Feel free to submit pull requests or share your feedback to help improve this tool further.

### Conclusion:

The YouTube Channel Data Extractor offers a convenient solution for extracting valuable insights from YouTube channels and their videos, empowering users with actionable data for analysis and decision-making. With its intuitive interface, robust functionality, and comprehensive test coverage, this project exemplifies the power of Python in harnessing APIs for data extraction and manipulation.

For detailed documentation and code comments, please refer to the individual files within the project repository.
