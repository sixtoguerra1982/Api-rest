**Comments:**

Read comments:

url:
GET /blog/<id>/get-comments/

**Response:**


```

[
    {
        "comment": "hi",
        "date": "2017-12-18T13:50:54.720648Z"
    }
]
```

if you use paginations (/blog/<id>/get-comments/?page=1):


```
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "comment": "hi",
            "date": "2017-12-18T13:50:54.720648Z"
        }
    ]
}
```

**Set likes:**

**Request:**

url:

POST /blog/1/set-like/

**Response:**

status=201