curl -X POST "http://localhost:8000/users/" \
     -H "Content-Type: application/json" \
     -d '{
           "email": "sadfagdsa@email.com",
           "username": "adhfda",
           "first_name": "zika",
           "last_name": "zikic",
           "gender": "m",
           "country": "us",
           "isActive": true,
           "password": "fdsa"
         }'