#!/bin/bash
#script causes the server to respond with a message containing You got me!, in the body of the response
#curl -s -u 98 -LX PUT 0.0.0.0:5000/catch_me -d 'You got me!'
#curl -s -LX PUT 0.0.0.0:5000/catch_me -w %{http_code}
#curl -X PUT -d 'user_id=98' 0.0.0.0:5000/catch_me
#curl -sL 0.0.0.0:5000/catch_me_2 -X PUT
#curl -sL 0.0.0.0:5000/catch_me -X PUT 'You got me!' -d 'user_id=98'
#curl -sLX OPTIONS 0.0.0.0:5000/catch_me -i
curl
