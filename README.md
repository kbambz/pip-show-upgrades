# pip-show-upgrades

Originally based on http://code.activestate.com/recipes/577708-check-for-package-updates-on-pypi-works-best-in-pi/

## Todo
- Convert to package
- Install to be runnable via 'pip-show-upgrades'
- Add conditional option support and functionality, such as for:
  - printing of upgrade commands
  - automatic running of upgrade commands
  - specify a preference for alpha/beta version handling

## Example Usage

```bash
$ python pip-show-upgrades.py 
cffi 1.6.0                               1.7.0 available
click 6.6                                up to date
cov-core 1.15.0                          up to date
coverage 4.1                             4.2 available
cryptography 1.3.2                       1.5 available
cycler 0.10.0                            up to date
ecdsa 0.13                               up to date
enum34 1.1.6                             up to date
et-xmlfile 1.0.1                         up to date
Fabric 1.11.1                            1.12.0 available
factory-boy 2.7.0                        up to date
fake-factory 0.5.7                       0.6.0 available
Flask 0.11                               0.11.1 available
funcsigs 1.0.2                           up to date
gspread 0.3.0                            0.4.1 available
httplib2 0.9.2                           up to date
idna 2.1                                 up to date
ipaddress 1.0.16                         up to date
itsdangerous 0.24                        up to date
jdcal 1.2                                up to date
Jinja2 2.8                               up to date
MarkupSafe 0.23                          up to date
matplotlib 1.5.1                         2.0.0b3, 2.0.0b2, 2.0.0b1, 1.5.2 available
memory-profiler 0.41                     up to date
mock 2.0.0                               up to date
nose2 0.6.4                              0.6.5 available
numpy 1.11.0                             1.11.1 available
oauth2client 2.1.0                       3.0.0 available
openpyxl 2.3.5                           2.4.0-b1, 2.4.0-a1 available
pandas 0.18.1                            up to date
paramiko 1.17.1                          2.0.2 available
pbr 1.9.1                                1.10.0 available
pip 8.1.2                                up to date
psutil 4.2.0                             4.3.0 available
pyasn1 0.1.9                             up to date
pyasn1-modules 0.0.8                     up to date
pycparser 2.14                           up to date
pycrypto 2.6.1                           up to date
pyOpenSSL 16.0.0                         16.1.0 available
pyparsing 2.1.4                          2.1.8 available
python-dateutil 2.5.3                    up to date
pytz 2016.4                              2016.6.1 available
requests 2.10.0                          2.11.1 available
rsa 3.4.2                                up to date
setuptools 21.0.0                        26.1.1 available
six 1.10.0                               up to date
Werkzeug 0.11.10                         up to date
xlrd 0.9.4                               1.0.0 available

pip install --upgrade cffi==1.7.0
pip install --upgrade coverage==4.2
pip install --upgrade cryptography==1.5
pip install --upgrade Fabric==1.12.0
pip install --upgrade fake-factory==0.6.0
pip install --upgrade Flask==0.11.1
pip install --upgrade gspread==0.4.1
pip install --upgrade matplotlib==2.0.0b3
pip install --upgrade matplotlib==2.0.0b2
pip install --upgrade matplotlib==2.0.0b1
pip install --upgrade matplotlib==1.5.2
pip install --upgrade nose2==0.6.5
pip install --upgrade numpy==1.11.1
pip install --upgrade oauth2client==3.0.0
pip install --upgrade openpyxl==2.4.0-b1
pip install --upgrade openpyxl==2.4.0-a1
pip install --upgrade paramiko==2.0.2
pip install --upgrade pbr==1.10.0
pip install --upgrade psutil==4.3.0
pip install --upgrade pyOpenSSL==16.1.0
pip install --upgrade pyparsing==2.1.8
pip install --upgrade pytz==2016.6.1
pip install --upgrade requests==2.11.1
pip install --upgrade setuptools==26.1.1
pip install --upgrade xlrd==1.0.0
