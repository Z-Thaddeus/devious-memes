<p align="center">
</p>

# Contents

1. [Requirements](#Requirements)
1. [Installation](#Installation)
1. [Variables](#Variables)
1. [Usage](#Usage)

# Requirements

The only Requirement you need is Python being installed.


# Installation

1. First start by setting up [Selenium](https://www.selenium.dev/documentation/webdriver/getting_started/).
1. Clone the project
1. Create a virtualenv
1. Install the requirements
1. Use the *youtube.py* file to download video.
1. Use the *connect_clips.py* to connect the videos into a compilation.

# Variables

## youtube.py
<table>
    <tr>
        <td>Field</td>
        <td>Explanation</td>
        <td>Default</td>
        <td>Datatype</td>
    </tr>
    <tr>
        <td><code>`IMPLICITLY_WAIT`</code></td>
        <td>Tell the selenium drive how long it should wait till the site fully loads (seconds).</td>
        <td>5</td>
        <td>int</td>
    </tr>
    <tr>
        <td><code>`INPUT_FILE`</code></td>
        <td>Location of the input file.</td>
        <td>input.txt</td>
        <td>string</td>
    </tr>
    <tr>
        <td><code>`MAX_SECONDS`</code></td>
        <td>Max video seconds.</td>
        <td>59</td>
        <td>int</td>
    </tr>
    <tr>
        <td><code>`MAX_MINUTES`</code></td>
        <td>Max video length.</td>
        <td>0</td>
        <td>int</td>
    </tr>
    <tr>
        <td><code>`DOWNLOAD_LOCATION`</code></td>
        <td>The location of where the videos should be downloaded.</td>
        <td>The default is the current folder with the date and month</td>
        <td>str</td>
    </tr>
    <tr>
</table>

## connect_clips.py
<table>
    <tr>
        <td>Field</td>
        <td>Explanation</td>
        <td>Default</td>
        <td>Datatype</td>
    </tr>
    <tr>
        <td><code>`VIDEO_LOCATION`</code></td>
        <td>Location of the videos you want to connect.</td>
        <td>None</td>
        <td>int</td>
    </tr>
    <tr>
        <td><code>`EXPORT_LOCATION`</code></td>
        <td>Location of the output location.</td>
        <td>youtube_video.mp4</td>
        <td>str</td>
    </tr>
</table>

**VIDEO_LOCATION** has to be set!

# Usage

Use the *youtube.py* file to download video.

```bash
$ python youtube.py
```

Use the *connect_clips.py* to connect the videos into a compilation.

```bash
$ python connect_clips.py
```