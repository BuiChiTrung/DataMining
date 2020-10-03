1. If using all scalar values, you must pass an index. Fix:
```
    df = pd.DataFrame({'a':1}, index = [52])
```
2. Quên cái ignore_index khi ghép các df vào nhau 
3. Dùng .loc khi đang trong vòng for => tle vcl
4. append mấy cái df trong vòng for (nên gom lại rồi append 1 phát)