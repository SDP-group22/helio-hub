from flask import render_template
from scheduler import Scheduler
from sensor_watcher import SensorWatcher
import connexion
import threading


def get_app():
    # Create the app instance
    app = connexion.App(__name__, specification_dir='./')

    # Read the api-spec.yml file to configure the endpoints
    app.add_api('api-spec.yml')

    # Hello world URL route at "/"
    @app.route('/')
    def home():
        return render_template('home.html')

    return app


if __name__ == '__main__':
    app = get_app()

    Scheduler.get_instance().start()
    SensorWatcher.get_instance().start()

    print('*********************  THREADS  **********************')
    for thread in threading.enumerate():
        print(thread.name)
    print('******************************************************')

    # serve the api
    app.run(host='0.0.0.0', port=4310, debug=True)