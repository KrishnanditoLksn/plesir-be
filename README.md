﻿# Plesir Recommendation System  REST API 

## GET ALL TRAVEL 

### 

GET  http://127.0.0.1:8000/destination/

```json
 "destination": [
        {
            "id": 1,
            "place_name": "Monumen Nasional",
            "description": "Monumen Nasional atau yang populer disingkat dengan Monas atau Tugu Monas adalah monumen peringatan setinggi 132 meter (433 kaki) yang didirikan untuk mengenang perlawanan dan perjuangan rakyat Indonesia untuk merebut kemerdekaan dari pemerintahan kolonial Hindia Belanda. Pembangunan monumen ini dimulai pada tanggal 17 Agustus 1961 di bawah perintah presiden Soekarno dan dibuka untuk umum pada tanggal 12 Juli 1975. Tugu ini dimahkotai lidah api yang dilapisi lembaran emas yang melambangkan semangat perjuangan yang menyala-nyala. Monumen Nasional terletak tepat di tengah Lapangan Medan Merdeka, Jakarta Pusat.",
            "category": "Budaya",
            "city": "Jakarta",
            "price": 20000.0,
            "hour": 0,
            "rating": 46
        }
]
```

## GET DETAIL TRAVEL AND SIMILAR ITEMS



GET  http://127.0.0.1:8000/destination/{id}/

```json
 "destination": {
        "id": 1,
        "place_name": "Monumen Nasional",
        "description": "Monumen Nasional atau yang populer disingkat dengan Monas atau Tugu Monas adalah monumen peringatan setinggi 132 meter (433 kaki) yang didirikan untuk mengenang perlawanan dan perjuangan rakyat Indonesia untuk merebut kemerdekaan dari pemerintahan kolonial Hindia Belanda. Pembangunan monumen ini dimulai pada tanggal 17 Agustus 1961 di bawah perintah presiden Soekarno dan dibuka untuk umum pada tanggal 12 Juli 1975. Tugu ini dimahkotai lidah api yang dilapisi lembaran emas yang melambangkan semangat perjuangan yang menyala-nyala. Monumen Nasional terletak tepat di tengah Lapangan Medan Merdeka, Jakarta Pusat.",
        "category": "Budaya",
        "city": "Jakarta",
        "price": 20000.0,
        "hour": 0,
        "rating": 46
    },
    "recommendations": [
        {
            "id": 259,
            "place_name": "Monumen Perjuangan Rakyat Jawa Barat",
            "description": "Monumen Perjuangan Rakyat Jawa Barat (Monju) adalah Museum Sejarah Perjuangan Rakyat Jawa Barat, di Tatar Pasundan atau Parahyangan. Monumen diresmikan oleh Gubernur Jawa Barat, Raden Nana Nuriana pada tanggal 23 Agustus 1995.",
            "category": "Budaya",
            "city": "Bandung",
            "price": 0.0,
            "hour": 0,
            "rating": 45
        },

 
