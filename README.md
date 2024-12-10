# DaddyLive Live TV & Sports Playlists

DaddyLive is a platform that offers free live TV and sports streaming across selected categories. Users can stream and watch live TV directly through their browser without the need for an account or subscription.

For added flexibility, this repository provides an M3U playlist featuring DaddyLive's channels. With this, you can load the streams into any IPTV application that supports M3U-formatted playlists.

You can view the full list of channels provided by DaddyLive [here](https://href.li/?https://dlhd.so/24-7-channels.php).

The latest events added to the playlist can be found [here](https://github.com/dtankdempse/daddylive-m3u/blob/main/events.txt).

**Note:** Adult channels have been excluded from the English playlist. If you wish to include these channels, the playlists can be found [here](https://github.com/dtankdempse/daddylive-m3u/tree/main/adult).

## Playlist Formats

---

### Standard Playlist Information

**Playlist.m3u8**  
This is a standard M3U playlist. To use it, ensure your IPTV application supports custom headers, specifically `Referer`, `Origin`, and `User-Agent`. These headers are required to access the streams, and omitting them will result in a 403 error.

#### Playlist URLs
- **English Only:** `https://bit.ly/ddy-m3u1`
- **All Regions:** `https://bit.ly/ddy-m3u1-all`
  
#### Guide URLs
- **EPG (XML):** `https://bit.ly/ddy-epg1`
- **EPG (GZ):** `https://bit.ly/ddy-epg1-gz`

#### Required Headers
- **Referer:** `https://cookiewebplay.xyz/`
- **Origin:** `https://cookiewebplay.xyz`
- **User-Agent:** `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36`

---

### TiviMate Playlist Information

- **tivimate_playlist.m3u8:**  
  This playlist is specifically formatted for use with TiviMate. Simply load the URL provided in this repository into TiviMate as an "M3U Playlist." No additional setup is needed, as TiviMate automatically manages the required headers for playback.

#### Playlist URLs
  - **English Only:** `https://bit.ly/ddy-m3u2`
  - **All Regions:** `https://bit.ly/ddy-m3u2-all`

#### Guide URLs
  - **EPG (XML):** `https://bit.ly/ddy-epg1`
  - **EPG (GZ):** `https://bit.ly/ddy-epg1-gz`

**Headers:** *(Automatically handled by TiviMate)*
  - **Referer:** `Included`
  - **Origin:** `Included`
  - **User-Agent:** `Included`
    
---

### Kodi Playlist Information    

- **kodi_playlist.m3u8:**  
  This playlist is designed for Kodi, utilizing `#KODIPROP` properties to handle the necessary stream settings, including the required headers. It is optimized for Kodi's PVR IPTV Simple Client, ensuring compatibility with your Kodi setup.

#### Playlist URLs
  - **English Only:** `https://bit.ly/ddy-m3u3`
  - **All Regions:** `https://bit.ly/ddy-m3u3-all`
  
#### Guide URLs
  - **EPG (XML):** `https://bit.ly/ddy-epg1`
  - **EPG (GZ):** `https://bit.ly/ddy-epg1-gz`

  **Headers:** *(Automatically handled by Kodi)*
  - **Referer:** `Included`
  - **Origin:** `Included`
  - **User-Agent:** `Included`

      
---

### VLC Playlist Information

- **vlc_playlist.m3u8:**  
  Optimized for VLC Media Player. This playlist uses VLC-specific formatting to ensure streams play correctly, including setting the necessary headers via `#EXTVLCOPT`.

#### Playlist URLs
  - **English Only:** `https://bit.ly/ddy-m3u4`
  - **All Regions:** `https://bit.ly/ddy-m3u4-all`

#### Guide URLs
  - **EPG (XML):** `https://bit.ly/ddy-epg1`
  - **EPG (GZ):** `https://bit.ly/ddy-epg1-gz`

  **Headers:** *(Automatically handled by VLC)*
  - **Referer:** `Included`
  - **Origin:** `Included`
  - **User-Agent:** `Included`

---

### Threadfin for Jellyfin, Plex, Emby Users    

If you prefer using the standard playlist version without an M3U Playlist Proxy, you can apply this FFmpeg profile in StreamMaster or Threadfin to watch the streams directly. This solution was shared by **@Tw1zT3d2four7** [here](https://github.com/dtankdempse/daddylive-m3u/issues/16#issuecomment-2466210425).

### M3U Playlist Proxy  

If none of these playlists work with your IPTV application, you can try using the [m3u-playlist-proxy](https://github.com/dtankdempse/m3u-playlist-proxy). This proxy acts as a middle layer to help resolve potential issues with playing the playlists, especially if your IPTV app doesn't support setting the required headers.

## Usage Instructions:

1. Choose the playlist format that suits your application or media player.
2. Add the playlist URL to your IPTV application.
3. Ensure that your application supports the required settings, such as setting the required headers for streams to play.

## Disclaimer:

This repository has no control over the streams, links, or the legality of the content provided by dlhd.so (including all mirror sites). It is the end user's responsibility to ensure the legal use of these streams, and we strongly recommend verifying that the content complies with the laws and regulations of your country before use.

