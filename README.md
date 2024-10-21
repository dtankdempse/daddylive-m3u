# DaddyLive Live TV & Sports Playlists

DaddyLive is a platform that offers free live TV and sports streaming across selected categories. Users can stream and watch live TV directly through their browser without the need for an account or subscription.

For added flexibility, this repository provides an M3U playlist featuring DaddyLive's channels. With this, you can load the streams into any IPTV application that supports M3U-formatted playlists.

You can view the full list of channels provided by DaddyLive [here](https://href.li/?https://dlhd.so/24-7-channels.php). 

**Note:** Adult channels have been excluded from the main playlist. If you wish to include these channels, the playlists can be found [here](https://github.com/dtankdempse/daddylive-m3u/tree/main/adult).

## Playlist Formats

---

### Standard Playlist Information

- **Playlist.m3u8:**
  A standard M3U playlist. If you're using this playlist, make sure your IPTV application allows the setting of a custom `Referer`, `Origin`, and `User-Agent` header. The headers must be set in order to access the streams. Failure to set the required headers will result in a 403 error when attempting to stream.

  - **Playlist URL:** `https://bit.ly/ddy-m3u1`  
  - **EPG URL:** `https://bit.ly/ddy-epg1`  

  **Headers Required:**
  - **Referer:** `https://ilovetoplay.xyz/`
  - **Origin:** `https://ilovetoplay.xyz`   
  - **User-Agent:** `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36`     

---

### TiviMate Playlist Information

- **tivimate_playlist.m3u8:**
  This playlist is specifically formatted for use with TiviMate. Simply load the URL provided in this repository into TiviMate as an "M3U Playlist." No additional setup is needed, as TiviMate handles the required headers for playback.

  - **Playlist URL:** `https://bit.ly/ddy-m3u2`  
  - **EPG URL:** `https://bit.ly/ddy-epg1`  

  **Headers:** *(Automatically handled by TiviMate)*
  - **Referer:** `Included`
  - **Origin:** `Included`
  - **User-Agent:** `Included`
    
---

### Kodi Playlist Information    

- **kodi_playlist.m3u8:**
  This playlist is designed for Kodi, utilizing `#KODIPROP` properties to handle the necessary stream settings, including the required headers. It is optimized for Kodi's PVR IPTV Simple Client, ensuring compatibility with your Kodi setup.

  - **Playlist URL:** `https://bit.ly/ddy-m3u3`  
  - **EPG URL:** `https://bit.ly/ddy-epg1`  

  **Headers:** *(Automatically handled by Kodi)*
  - **Referer:** `Included`
  - **Origin:** `Included`
  - **User-Agent:** `Included`
      
---

### VLC Playlist Information

- **vlc_playlist.m3u8:**
  Optimized for VLC Media Player. This playlist uses VLC-specific formatting to ensure streams play correctly, including setting the necessary headers via `#EXTVLCOPT`.

  - **Playlist URL:** `https://bit.ly/ddy-m3u4`  
  - **EPG URL:** `https://bit.ly/ddy-epg1`  

  **Headers:** *(Automatically handled by VLC)*
  - **Referer:** `Included`
  - **Origin:** `Included`
  - **User-Agent:** `Included`


If none of these playlists work with your IPTV application, you can try using the [m3u-playlist-proxy](https://github.com/dtankdempse/m3u-playlist-proxy). This proxy acts as a middle layer to help resolve potential issues with playing the playlists, especially if your IPTV app doesn't support setting the required headers.

## Usage Instructions:

1. Choose the playlist format that suits your application or media player.
2. Add the playlist URL to your IPTV application.
3. Ensure that your application supports the required settings, such as setting the required headers for streams to play.

## Disclaimer:

This repository has no control over the streams, links, or the legality of the content provided by dlhd.so (including all mirror sites). It is the end user's responsibility to ensure the legal use of these streams, and we strongly recommend verifying that the content complies with the laws and regulations of your country before use.

