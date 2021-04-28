# Utility Commands

## Contents

1) [Convert Videos to GIF](www.link1)

---

## Convert Videos to GIF

The conversion is really handy (hint: animation in GitHub markdown people!).

---

**Package required:** ffmpeg

**Description:** 

`ffmpeg` is one of the most powerful utilities out there to work
with audio/video file formats, no question.

**Usage:**

```bash
$ ffmpeg -ss 00:00:05 -t 4 -i video.mp4 output.gif
$ ffmpeg -ss 00:00:05 -t 4 -vf "fps=30,scale=640:-1:flags=lanczos" -i video.mp4 output.gif
```

---

