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

---
<details>
<summary>Click to read Disclaimer.</summary>
  
## Disclaimer:

This repository has no control over the streams, links, or the legality of the content provided by dlhd.so (including all mirror sites). It is the end user's responsibility to ensure the legal use of these playlists, and we strongly recommend verifying that the content complies with the laws and regulations of your country before use.
</details>

<details>
<summary>Click to read DMCA Notice.</summary>

## DMCA Notice:

This repository does not host or store any video files. It simply organizes publicly accessible web links, which can be accessed through a web browser, into an M3U-formatted playlist. To the best of our knowledge, the content was intentionally made publicly available by the copyright holders or with their permission and consent granted to these websites to stream and share the content they provide.

Please note that linking does not directly infringe copyright, as no copies are made on this repository or its servers. Therefore, sending a DMCA notice to GitHub or the maintainers of this repository is not a valid course of action. To remove the content from the web, you should contact the website or hosting provider actually hosting the material.

If you still believe a link infringes on your rights, you can request its removal by opening an [issue](https://github.com/dtankdempse/daddylive-m3u/issues) or submitting a [pull request](https://github.com/dtankdempse/daddylive-m3u/pulls). Be aware, however, that removing a link here will not affect the content hosted on the external websites, as this repository has no control over the files or the content being provided.

</details>
