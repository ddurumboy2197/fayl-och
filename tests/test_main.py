Pytest uchun:
```python
import pytest
from unittest.mock import Mock
from your_module import read_txt_file

def test_read_txt_file():
    with open('test.txt', 'w') as f:
        f.write('Hello, World!')

    result = read_txt_file('test.txt')
    assert result == 'Hello, World!'

    with pytest.raises(FileNotFoundError):
        read_txt_file('non_existent_file.txt')

    with open('test.txt', 'w') as f:
        f.write('')

    result = read_txt_file('test.txt')
    assert result == ''

    with open('test.txt', 'w') as f:
        f.write('   ')

    result = read_txt_file('test.txt')
    assert result.strip() == ''
```

Jest uchun:
```javascript
import { readTxtFile } from './your_module';

describe('readTxtFile', () => {
  it('should read file with content', () => {
    const fs = require('fs');
    fs.writeFileSync('test.txt', 'Hello, World!');
    const result = readTxtFile('test.txt');
    expect(result).toBe('Hello, World!');
    fs.unlinkSync('test.txt');
  });

  it('should throw error for non-existent file', () => {
    expect(() => readTxtFile('non_existent_file.txt')).toThrowError();
  });

  it('should return empty string for empty file', () => {
    const fs = require('fs');
    fs.writeFileSync('test.txt', '');
    const result = readTxtFile('test.txt');
    expect(result).toBe('');
    fs.unlinkSync('test.txt');
  });

  it('should return empty string for file with only whitespace', () => {
    const fs = require('fs');
    fs.writeFileSync('test.txt', '   ');
    const result = readTxtFile('test.txt');
    expect(result.trim()).toBe('');
    fs.unlinkSync('test.txt');
  });
});
```
