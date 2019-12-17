#!/bin/bash

if command -v python3 &>/dev/null; then
    echo "Python 3 is installed"
else
    echo "Please, install python3 then rerun the script"
fi

if command -v pip3 &>/dev/null; then
    echo "Pip 3 is installed"
else
    echo "Please, install pip3 then rerun the script"
fi

pip3 install -r requirements.txt

cd backend/

if [ -f "cine_view.db"]; then
  echo "Please run the command sqlite3 cine_view.db in the backend folder!!!"
  exit
fi

if [ -d "venv" ]; then
  echo "The Virtualenv exists"
else
  virtualenv -p python3 venv
fi

source venv/bin/activate
pip3 install -r requirements.txt
deactivate

cd ../frontend

if [ -d "venv" ]; then
  echo "The Node virtualenv exists"
else
  nodeenv --without-ssl env
fi

source env/bin/activate

npm install -g vue
npm install -g @vue/cli
npm install vue-chartjs chart.js --save
npm install axios@0.18.0 --save
npm install bootstrap@4.3.1 --save
npm install vue-slider-component --save
npm i --save @fortawesome/fontawesome-svg-core
npm i --save @fortawesome/free-solid-svg-icons
npm i --save @fortawesome/vue-fontawesome
npm install --save vue-lodash
npm audit fix

deactivate_node
