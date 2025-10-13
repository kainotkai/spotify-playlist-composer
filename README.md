# spotify-playlist-composer
A Python-based application that leverages the Spotify API to read, analyze, and manipulate playlists using object-oriented programming principles.

## Overview

This project provides an extensible framework for working with Spotify playlists programmatically. By implementing OOP design patterns, it allows you to create custom playlist types, extend base functionality, and compose complex playlist operations.

## Features

- **Playlist Reading**: Fetch and parse playlist data from Spotify
- **OOP Architecture**: Extensible playlist classes using inheritance and composition
- **Playlist Operations**: Perform various operations on playlist data
- **Custom Extensions**: Easily create specialized playlist types for specific use cases

## Technologies Used

- **Python 3.x**
- **Spotipy**: Python library for the Spotify Web API
- **Spotify API**: Access to Spotify's music catalog and user data

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/spotify-playlist-manager.git
cd spotify-playlist-manager
```

2. Install required dependencies:
```bash
pip install spotipy
```

3. Set up Spotify API credentials:
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
   - Create a new application
   - Note your `Client ID` and `Client Secret`
   - Set your redirect URI (e.g., `http://localhost:8080`)

4. Configure authentication:
```python
# Create a .env file or export environment variables
SPOTIPY_CLIENT_ID='your-client-id'
SPOTIPY_CLIENT_SECRET='your-client-secret'
SPOTIPY_REDIRECT_URI='http://localhost:8080'
```


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Spotipy Documentation](https://spotipy.readthedocs.io/)
- [Spotify Web API Reference](https://developer.spotify.com/documentation/web-api/)

## Contact

Your Name - kait069111@gmail.com
