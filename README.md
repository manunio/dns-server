## config
* api is for nginx
* api.service is for systemctl

## cron script for git commit & push
`*/15 * * * * /bin/bash -l -c 'cd /home/maxx/api/ && /usr/bin/git add . && /usr/bin/git commit -m "update log" && /usr/bin/git push origin master'`
