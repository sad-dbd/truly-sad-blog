#!/usr/bin/env python3
import os, html, re

BASE = os.path.dirname(os.path.abspath(__file__))
INPUT = os.path.join(BASE, 'input')

def to_html(text):
    out = []
    for line in text.strip().split('\n'):
        s = line.strip()
        if s:
            out.append(f'<span class="lyric-line">{html.escape(s)}</span>')
        else:
            out.append('<span class="lyric-break"></span>')
    return ''.join(out)

NAV = '''\
<body><nav class="nav">
  <a class="wordmark" href="/">:(</a>
  <div class="nav-links">
    <a class="nav-link" href="/untitled/">Untitled</a>
    <a class="nav-link active" href="/releases/">Releases</a>
    <a class="nav-link" href="/studios/">Studios</a>
    <a class="nav-link external" href="https://sadcollection.com" target="_blank" rel="noopener">Collections</a>
  </div>
  <button class="hamburger" id="hamburger" onclick="toggleMenu()" aria-label="Menu">
    <span></span><span></span><span></span>
  </button>
</nav>
<div class="mobile-menu" id="mobile-menu">
  <a class="nav-link" href="/untitled/">Untitled</a>
  <a class="nav-link" href="/releases/">Releases</a>
  <a class="nav-link" href="/studios/">Studios</a>
  <a class="nav-link external" href="https://sadcollection.com" target="_blank" rel="noopener">Collections</a>
</div>'''

FOOTER = '''\
<footer class="footer">
  <div class="footer-copy">© 2023–2026 SAD Ventures Limited</div>
  <div class="footer-links">
    <a class="footer-link" href="https://open.spotify.com/artist/5hGsyji228sxPvOgRmqB62?si=cnXK65KESEeiuKkkVc1ieQ" target="_blank" rel="noopener">Spotify</a>
    <a class="footer-link" href="https://music.apple.com/nz/artist/s-ad/1810440438" target="_blank" rel="noopener">Apple Music</a>
    <a class="footer-link" href="https://www.youtube.com/channel/UClng_uh6ncoHfBFMhzNdmZw" target="_blank" rel="noopener">Youtube</a>
    <a class="footer-link" href="https://www.instagram.com/_trulysad/" target="_blank" rel="noopener">Instagram</a>
  </div>
</footer>'''

SCRIPT = '''\
<script>
  function toggleMenu(){document.getElementById('hamburger').classList.toggle('open');document.getElementById('mobile-menu').classList.toggle('open');}
  function closeMenu(){document.getElementById('hamburger').classList.remove('open');document.getElementById('mobile-menu').classList.remove('open');}
</script>'''

def page(slug, title, date, producer, apple, spotify_url, youtube, spotify_id, lyrics_html):
    t = html.escape(title)
    gtag = "window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-EV2ME4P7XY');"
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{t} Lyrics - S.AD</title>
  <meta name="description" content="Lyrics for {t} by S.AD.">
  <link rel="canonical" href="https://trulysad.com/lyrics/{slug}/">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' fill='black'/><text y='78' x='50' font-size='72' text-anchor='middle' fill='white' font-family='monospace'>:(</text></svg>">
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-EV2ME4P7XY"></script>
  <script>{gtag}</script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@300;400;500&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/sad.css">
</head>
{NAV}
<main>
  <div class="lyrics-wrap fade-in">
    <a class="back-link" href="/releases/">Back to Releases</a>
    <div class="track-eyebrow">S.AD - {date}</div>
    <div class="track-title">{t}</div>
    <div class="track-credits">Produced by {html.escape(producer)}</div>
    <div class="lyrics-dsp-section">
      <div class="dsp-links">
        <a class="dsp-link" href="{apple}" target="_blank" rel="noopener">Apple Music</a>
        <a class="dsp-link" href="{spotify_url}" target="_blank" rel="noopener">Spotify</a>
        <a class="dsp-link" href="{youtube}" target="_blank" rel="noopener">Youtube Music</a>
      </div>
    </div>
    <div class="lyrics-body">{lyrics_html}</div>
  </div>
</main>
<div class="player-bar">
  <iframe src="https://open.spotify.com/embed/album/{spotify_id}?utm_source=generator&theme=0"
    width="100%" height="80" frameborder="0" allowtransparency="true" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
    loading="lazy"></iframe>
</div>
{FOOTER}{SCRIPT}</body></html>'''

TRACKS = [
    dict(slug='anon',          title='ANON',           date='30 Apr 2025', producer='Eliezer Apfel',
         apple='https://music.apple.com/nz/album/anon-single/1810484215',
         spotify_url='https://open.spotify.com/album/7y3osUClWl8Nexdv0otqTA?si=FYHcBCwoRfqX0aI-6mKSwQ',
         spotify_id='7y3osUClWl8Nexdv0otqTA',
         youtube='https://music.youtube.com/watch?v=SEr16YUh2B8&si=PKmuuGypUuvZhWkM',
         file='sad_anon_lyrics.txt'),
    dict(slug='morals',        title='Morals',          date='01 Oct 2025', producer='Eliezer Apfel',
         apple='https://music.apple.com/nz/album/morals-single/1831315341',
         spotify_url='https://open.spotify.com/album/4w8eTXC9AbaHI5BdEzpP2G?si=kgitUqJzSE2lN3dte4gCZA',
         spotify_id='4w8eTXC9AbaHI5BdEzpP2G',
         youtube='https://music.youtube.com/watch?v=YvKa4S9_oyg&si=6zki-LYuLP7DmucO',
         file='sad_morals_lyrics.txt'),
    dict(slug='doomed',        title='Doomed',          date='20 Dec 2025', producer='Ten.Oh',
         apple='https://music.apple.com/nz/album/doomed-single/1857787358',
         spotify_url='https://open.spotify.com/album/4nYMESdOzmcIJNObmPqyhc?si=f96bEayIQJ600g6p69jRtQ',
         spotify_id='4nYMESdOzmcIJNObmPqyhc',
         youtube='https://music.youtube.com/watch?v=t-AAdjbOYi4&si=Q9f-kOziiAIM1yKs',
         file='sad_doomed_lyrics.txt'),
    dict(slug='ampersand',     title='&',               date='01 Sep 2025', producer='Eliezer Apfel',
         apple='https://music.apple.com/nz/album/single/1831297753',
         spotify_url='https://open.spotify.com/album/383HydEzbrzOTOtXwtRWwd?si=jBA1tJ9yTw2bDrxDOEvDHA',
         spotify_id='383HydEzbrzOTOtXwtRWwd',
         youtube='https://music.youtube.com/watch?v=pS5qWivnqKc&si=3GtznO4BATHGw1iU',
         file='sad_&_lyrics.txt'),
    dict(slug='faded',         title='Faded',           date='14 Jun 2025', producer='Eliezer Apfel',
         apple='https://music.apple.com/nz/album/faded-single/1817879772',
         spotify_url='https://open.spotify.com/album/4bs9oY2ZYgCP5b5SqkbSwZ?si=UrKWTs26Rv-5VmlgYreOrw',
         spotify_id='4bs9oY2ZYgCP5b5SqkbSwZ',
         youtube='https://music.youtube.com/watch?v=D2KdT8dgvHg&si=zJ9NpXqVRZ5toMvZ',
         file='sad_faded_lyrics.txt'),
    dict(slug='lo',            title='Lo',              date='31 Dec 2025', producer='Eliezer Apfel',
         apple='https://music.apple.com/nz/album/lo-doomed-faded/1857636519',
         spotify_url='https://open.spotify.com/album/3hVhExInvfNSkEo9ezOSsq?si=ISF3ClcPQaW6oba2GFgIyA',
         spotify_id='3hVhExInvfNSkEo9ezOSsq',
         youtube='https://music.youtube.com/playlist?list=OLAK5uy_nYbVmqTYMdK_EiVigg9khaC9ZphlQp31g&si=aLBfmXzC4QC9SEoR',
         file='01_sad_lo_lyrics.txt'),
    dict(slug='where-do-we-go', title='where do we go', date='31 Dec 2025', producer='Eliezer Apfel',
         apple='https://music.apple.com/nz/album/lo-doomed-faded/1857636519',
         spotify_url='https://open.spotify.com/album/3hVhExInvfNSkEo9ezOSsq?si=ISF3ClcPQaW6oba2GFgIyA',
         spotify_id='3hVhExInvfNSkEo9ezOSsq',
         youtube='https://music.youtube.com/playlist?list=OLAK5uy_nYbVmqTYMdK_EiVigg9khaC9ZphlQp31g&si=aLBfmXzC4QC9SEoR',
         file='07_sad_where_do_we_go_lyrics.txt'),
]

for t in TRACKS:
    lyrics_text = open(os.path.join(INPUT, t['file'])).read()
    lyrics_html = to_html(lyrics_text)
    html_out = page(t['slug'], t['title'], t['date'], t['producer'], t['apple'],
                    t['spotify_url'], t['youtube'], t['spotify_id'], lyrics_html)
    out_dir = os.path.join(BASE, t['slug'])
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'index.html')
    with open(out_path, 'w') as f:
        f.write(html_out)
    print(f'wrote {out_path}')

print('done')
