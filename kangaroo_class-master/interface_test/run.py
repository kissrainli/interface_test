import re
import sys

from httprunner.cli import main

if __name__ == '__main__':
    # sys.argv.append('testcases/test_shanxi.yml')
    sys.argv.append('testsuites/test_shanxi.yml')
    sys.argv.append('--dot-env-path=.env-shanxi')
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
