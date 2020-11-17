# 🔊 Play sounds after shell jobs complete

`ding` is command-line utility that will play a sound after a long job completes.

The utility will take data that is piped into its standard inputs and pipe it to standard output. That is to say that data piped into `ding` will be piped right back out.

```bash
$ echo "Hello!" | ding
Hello!
```

As a result, you can build pipelines with `ding`.

For example, you can download an ISO with [`http`](https://httpie.org/), visualize the progress with [`pv`](http://www.ivarch.com/programs/pv.shtml), and when it's finished, play a sound with `ding`.

```bash
$ export URL="https://releases.ubuntu.com/20.04.1/ubuntu-20.04.1-desktop-amd64.iso"
$ http "$URL" | pv | ding > /dev/null
```

This project uses [`play_sounds`](https://github.com/alexdelorenzo/play_sounds), a wrapper over [`playsound`](https://pypi.org/project/playsound/) and [`boombox`](https://pypi.org/project/boombox/).

## `ding`

You can either set the `$DING` environment variable to the sound you'd like to play, or supply the sound with the `-s` flag.

```bash
# You can run ding after a command or as part of a pipeline
$ export DING="~/Music/ding.ogg"
$ sleep 5; ding
$ echo "Hello!" | ding
Hello!
```

This allows you to set `$DING` in your `~/.bashrc`.

You can also specify it with a flag.

```bash
$ echo "Hello!" | ding -s ding.ogg
Hello!
```

`ding` comes with a default sound that will play if neither `$DING` or `-s` are set. You can use the `-w` flag to show warnings if `$DING` or `-s` are not set.

```bash
$ echo "Hello!" | ding
Hello!
```

# Installation
## Dependencies
 - A Unix shell like Bash
 - Python 3.6+
 - `requirements.txt`

### Linux
 - GStreamer

On Ubuntu, you will need to install `PyGObject`, `gstreamer1.0-python3-plugin-loader` and `python3-gst-1.0`.

```bash
sudo apt install python3-gi gstreamer1.0-python3-plugin-loader python3-gst-1.0
```

## PyPI
```bash
$ python3 -m pip install onhold_ding
```

## GitHub
```bash
$ python3 -m pip install -r requirements.txt
$ python3 setup.py install
```

# Help
## `ding`
```bash
$ ding --help
Usage: ding [OPTIONS]

  Play specified sound after job is complete.

Options:
  -s, --sound_path PATH  Path to sound to play.
  -i, --ignore           Suppress warnings.
  --help                 Show this message and exit.
```

# License
See `LICENSE`. If you'd like to use this project with a different license, please get in touch.


# Credit
## Music

See [`CREDIT.md`](/CREDIT.md).
