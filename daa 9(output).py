Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
================ RESTART: C:\Users\saranya\Desktop\DAA\daa 9.py ================
Items: [0.5, 0.7, 0.3, 0.9, 0.2, 0.6, 0.8, 0.4, 0.1, 0.5]
Capacity: 1.0
Sum of items: 5.0
Lower bound on bins: 5

First Fit (FF): 6 bins
 Bin 1: [0.5, 0.3, 0.2] | Used: 1.0 [####################]
 Bin 2: [0.7, 0.1] | Used: 0.8 [###############     ]
 Bin 3: [0.9] | Used: 0.9 [##################  ]
 Bin 4: [0.6, 0.4] | Used: 1.0 [####################]
 Bin 5: [0.8] | Used: 0.8 [################    ]
 Bin 6: [0.5] | Used: 0.5 [##########          ]

First Fit Decreasing (FFD): 6 bins
 Bin 1: [0.9] | Used: 0.9 [##################  ]
 Bin 2: [0.8, 0.1] | Used: 0.9 [##################  ]
 Bin 3: [0.7, 0.3] | Used: 1.0 [####################]
 Bin 4: [0.6, 0.4] | Used: 1.0 [####################]
 Bin 5: [0.5, 0.5] | Used: 1.0 [####################]
 Bin 6: [0.2] | Used: 0.2 [####                ]

Best Fit Decreasing (BFD): 6 bins
 Bin 1: [0.9] | Used: 0.9 [##################  ]
 Bin 2: [0.8, 0.1] | Used: 0.9 [##################  ]
 Bin 3: [0.7, 0.3] | Used: 1.0 [####################]
 Bin 4: [0.6, 0.4] | Used: 1.0 [####################]
 Bin 5: [0.5, 0.5] | Used: 1.0 [####################]
 Bin 6: [0.2] | Used: 0.2 [####                ]

Summary:
Lower Bound = 5
FF  = 6 bins
FFD = 6 bins
BFD = 6 bins
