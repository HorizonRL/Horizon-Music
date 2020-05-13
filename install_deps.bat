python -m pip install --upgrade pip wheel setuptools virtualenv
python -m virtualenv env
call env\Scripts\activate

python -m pip install docutils pygments pypiwin32 kivy_deps.sdl2==0.1.* kivy_deps.glew==0.1.*
python -m pip install kivy_deps.gstreamer==0.1.*
python -m pip install kivy_deps.angle==0.1.*

python -m pip install kivy==1.11.1

pip install pycaw