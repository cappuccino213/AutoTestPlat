var locust=
[
    {
        "need": 1,
        "parameter": "--host=127.0.0.1",
        "description": "Host to load test in the following format: http://10.21.32.33"
    },
    {
        "need": 1,
        "parameter": "--web-host=192.168.1.56",
        "description": "Host to bind the web interface to. Defaults to '' (all interfaces)"
    },
    {
        "need": 1,
        "parameter": "--web-port=8182",
        "description": "Port on which to run web host"
    },
    {
        "need": 0,
        "parameter": "--csv=CSVFILEBASE",
        "description": "Store current request stats to files in CSV format."
    },
    {
        "need": 0,
        "parameter": "--master",
        "description": "Set locust to run in distributed mode with this process as master"
    },
    {
        "need": 0,
        "parameter": "--slave",
        "description": "Set locust to run in distributed mode with this process as slave"
    },
    {
        "need": 0,
        "parameter": "--master-host=MASTER_HOST",
        "description": "Host or IP address of locust master for distributed load testing. Only used when running with --slave.Defaults to 127.0.0.1"
    },
    {
        "need": 0,
        "parameter": "--master-port=MASTER_HOST",
        "description": "The port to connect to that is used by the locust master for distributed load testing. Only used when running with --slave. Defaults to 5557. Note that slaves will also connect to the master node on this port + 1"
    },
    {
        "need": 0,
        "parameter": "--master-bind-host=MASTER_BIND_HOST",
        "description": "Interfaces (hostname, ip) that locust master should bind to. Only used when running with --master. Defaults to * (all available interfaces)"
    },
    {
        "need": 0,
        "parameter": "--master-bind-port=MASTER_BIND_PORT",
        "description": "Port that locust master should bind to. Only used when running with --master. Defaults to 5557. Note that Locust will also use this port + 1, so by default the  master node will bind to 5557 and 5558"
    },
    {
        "need": 0,
        "parameter": "--expect-slaves=EXPECT_SLAVES",
        "description": "How many slaves master should expect to connect before starting the test (only when --no-web used)."
    },
    {
        "need": 0,
        "parameter": "--no-web",
        "description": "Disable the web interface, and instead start running the test immediately. Requires -c and -r to be specified"
    },
    {
        "need": 0,
        "parameter": "--clients=NUM_CLIENTS",
        "description": "Number of concurrent clients. Only used together with --no--web"
    },
    {
        "need": 0,
        "parameter": "--hatch-rate=HATCH_RATE",
        "description": "The rate per second in which clients are spawned. Only used together with --no-web"
    },
    {
        "need": 0,
        "parameter": "--num-request=NUM_REQUESTS",
        "description": "Number of requests to perform. Only used together with --no-web"
    },
    {
        "need": 0,
        "parameter": "--loglevel=LOGLEVEL",
        "description": "Choose between DEBUG/INFO/WARNING/ERROR/CRITICAL. Default is INFO."
    },
    {
        "need": 0,
        "parameter": "--logfile=LOGFILE",
        "description": "Path to log file. If not set, log will go to stdout/stderr"
    },
    {
        "need": 0,
        "parameter": "--print-stats",
        "description": "Print stas in the console"
    },
    {
        "need": 0,
        "parameter": "--only-summary",
        "description": "Only print the summary stats"
    },
    {
        "need": 0,
        "parameter": "--no-reset-stats",
        "description": "Do not reset statistics once hatching has been completed"
    },
    {
        "need": 0,
        "parameter": "-list",
        "description": "Show list of possible locust classes and exit"
    },
    {
        "need": 0,
        "parameter": "--show-task-ratio",
        "description": "print table of the locust classes' task execution ratio"
    },
    {
        "need": 0,
        "parameter": "--show-task-ratio-json",
        "description": "print json data of the locust classes' task execution ratio"
    },
    {
        "need": 0,
        "parameter": "--version",
        "description": "show program's version number and exit"
    }
]