# urllist2labelx
转换urllist为符合labelx输入格式的jsonlist

## Usage
### format
urllist file:
```
http://available_host/path1.jpg
http://available_host/path2.jpg
http://available_host/path3.jpg
http://available_host/path4.jpg
```

### generate detect jsonlist

```python
python detect-init.py urltest.list
```

### generate classify jsonlist

```python
python classify-init.py urltest.list
```