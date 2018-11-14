Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================

Warning (from warnings module):
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/font_manager.py", line 281
    'Matplotlib is building the font cache using fc-list. '
UserWarning: Matplotlib is building the font cache using fc-list. This may take a moment.

===================== RESTART: /home/user/RTR105/1B1.py =====================

=================== RESTART: /home/user/RTR105/1B1(sin).py ===================
Traceback (most recent call last):
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/colors.py", line 132, in to_rgba
    rgba = _colors_full_map.cache[c, alpha]
KeyError: ('FF0000', None)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/backends/backend_qt5agg.py", line 164, in __draw_idle_agg
    self.draw()
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/backends/backend_qt5agg.py", line 133, in draw
    super(FigureCanvasQTAggBase, self).draw()
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/backends/backend_agg.py", line 430, in draw
    self.figure.draw(self.renderer)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/artist.py", line 55, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/figure.py", line 1299, in draw
    renderer, self, artists, self.suppressComposite)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/image.py", line 138, in _draw_list_compositing_images
    a.draw(renderer)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/artist.py", line 55, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/axes/_base.py", line 2437, in draw
    mimage._draw_list_compositing_images(renderer, self, artists)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/image.py", line 138, in _draw_list_compositing_images
    a.draw(renderer)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/artist.py", line 55, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/lines.py", line 767, in draw
    ln_color_rgba = self._get_rgba_ln_color()
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/lines.py", line 1269, in _get_rgba_ln_color
    return mcolors.to_rgba(self._color, self._alpha)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/colors.py", line 134, in to_rgba
    rgba = _to_rgba_no_colorcycle(c, alpha)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/colors.py", line 178, in _to_rgba_no_colorcycle
    raise ValueError("Invalid RGBA argument: {!r}".format(orig_c))
ValueError: Invalid RGBA argument: 'FF0000'

=================== RESTART: /home/user/RTR105/1B1(sin).py ===================
Traceback (most recent call last):
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/colors.py", line 132, in to_rgba
    rgba = _colors_full_map.cache[c, alpha]
KeyError: ('FF0000', None)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/backends/backend_qt5agg.py", line 164, in __draw_idle_agg
    self.draw()
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/backends/backend_qt5agg.py", line 133, in draw
    super(FigureCanvasQTAggBase, self).draw()
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/backends/backend_agg.py", line 430, in draw
    self.figure.draw(self.renderer)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/artist.py", line 55, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/figure.py", line 1299, in draw
    renderer, self, artists, self.suppressComposite)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/image.py", line 138, in _draw_list_compositing_images
    a.draw(renderer)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/artist.py", line 55, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/axes/_base.py", line 2437, in draw
    mimage._draw_list_compositing_images(renderer, self, artists)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/image.py", line 138, in _draw_list_compositing_images
    a.draw(renderer)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/artist.py", line 55, in draw_wrapper
    return draw(artist, renderer, *args, **kwargs)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/lines.py", line 767, in draw
    ln_color_rgba = self._get_rgba_ln_color()
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/lines.py", line 1269, in _get_rgba_ln_color
    return mcolors.to_rgba(self._color, self._alpha)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/colors.py", line 134, in to_rgba
    rgba = _to_rgba_no_colorcycle(c, alpha)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/colors.py", line 178, in _to_rgba_no_colorcycle
    raise ValueError("Invalid RGBA argument: {!r}".format(orig_c))
ValueError: Invalid RGBA argument: 'FF0000'

=================== RESTART: /home/user/RTR105/1B1(sin).py ===================

===================== RESTART: /home/user/RTR105/1B1.py =====================

=================== RESTART: /home/user/RTR105/1B1(sin).py ===================

=================== RESTART: /home/user/RTR105/1B1(sin).py ===================

=================== RESTART: /home/user/RTR105/1B1(sin).py ===================

=================== RESTART: /home/user/RTR105/1B1(sin).py ===================

===================== RESTART: /home/user/RTR105/1B1.py =====================
>>> 
