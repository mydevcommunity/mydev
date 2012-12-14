Title: Automated Testing Dalam Pembangunan Perisian
Tags: testing, automated

_Testing_ adalah sebahagian daripada proses pembangunan perisian komputer. Setiap kali baris-baris kod ditulis, diubah atau dipadam, ia mesti melalui proses testing bagi memastikan program tersebut masih lagi berjalan sebagaimana yang diharapkan. Ini bermakna kita sama sekali tidak boleh mengelak daripada melakukan _testing_ terhadap program atau aplikasi yang kita bangunkan.

## Manual Testing
Testing biasanya dilakukan secara manual dengan pengaturcara cuba menjalankan aturcara atau aplikasi yang dibangunkan dan memerhatikan sama ada ia mengeluarkan output yang dikehendaki ataupun semua _features_ berfungsi sebagai mana diharapkan. Ambil contoh aturcara ringkas berikut:-

```python
    function add(num1, num2) {
        return num1 + num2;
    }

    print add(1, 2) . "\n" # akan paparkan 3
    print add(2, 2) . "\n" # akan paparkan 4
```

Andaikan aturcara diatas ditulis menggunakan bahasa PHP dan disimpan dalam fail bernama `add.php`. Untuk menguji aturcara ini, pengaturcara akan `execute` fail tersebut dan memerhatikan sama ada ia memaparkan out yang diharapkan iaitu:-

    3
    4

Aturcara tersebut mungkin boleh dijalankan seperti berikut:-

```bash
    php add.php
    3
    4
```

Di atas kita dapati aturcara tersebut memaparkan output yang kita kehendaki. Sekarang kita andaikan berlaku sedikit kesilapan dalam kod tersebut. Katakan ia ditulis seperti berikut:-

```python
    function add(num1, num2) {
        return num1 * num2;
    }

    print add(1, 2) . "\n"; # akan paparkan 3
    print add(2, 2) . "\n"; # akan paparkan 4
```

Apabila dijalankan, kita akan dapati outputnya berlainan:-

    2
    4

Ini bermakna program tersebut gagal dalam proses _testing_ kita. Cara _testing_ seperti diatas walaupun mudah untuk difahami dan diamalkan ia menjadi amat tidak efektif apabila program semakin berkembang dan kompleks. Ia juga tidak efektif kerana bergantung semata-mata kepada keupayaan mata kita untuk mengesan perbezaan pada output yang dipaparkan. Bukan mahu menidakkan keupayaan mata namun manusia sememangnya tidak sesuai untuk melakukan kerja-kerja leceh dan remeh seperti ini. Disinilah fungsi komputer supaya manusia boleh menumpukan kepada kerja-kerja yang lebih memerlukan daya fikir, intelek serta kreativiti yang tinggi.

## Automated Testing
Dalam proses _testing_ secara manual di atas, kita bergantung kepada tenaga manusia untuk memerhatikan semasa program dijalankan, ia menghasilkan output yang dikehendaki atau tidak. Dalam _automated testing_ kita akan menulis satu aturcara lain bagi menguji aturcara yang dibangunkan. Ini membolehkan kita untuk _delegate_ tugas-tugas menguji tersebut kepada komputer yang sudah semestinya lebih efisyen untuk melaksanakannya.

Contoh kod sebelum ini boleh ditulis seperti berikut untuk <fill in>:-

```php
    function add($num1, $num2) {
        return $num1 * $num2;
    }

    assert(add(1, 2) === 3);
    assert(add(2, 2) === 4);
```

Apabila dijalankan kita akan melihat output seperti berikut:-

    Warning: assert(): Assertion failed in /home/rkiteratai/add.php on line 6

Aah, sekarang anda sudah dapat melihat bagaimana komputer sudah mula mengambil peranan manusia dalam menguji kod aturcara.

Kod automated testing boleh ditulis dengan 2 cara, sama ada selepas kod aturcara perisian siap ditulis atau sebelum kod aturcara perisian ditulis.

## Kategori _Test_
* Unit Test
* Functional Test
* Integration Test
* Stress Test

## Test Framework
...

## Contoh Test mengikut bahasa pengaturcaraan

### Unit Test dalam C# (.NET)

Dalam dunia .NET, antara _unit testing framework_ yang paling awal dan paling meluas digunakan ialah NUnit. Berikut adalah contoh bagaimana ia digunakan.

Katakan kod yang ingin diuji adalah seperti berikut:

```csharp
class Calculator
{
    public int Add(int operand1, int operand2)
    {
        return operand1 + operand2;
    }

    public int Minus(int operand1, int operand2)
    {
        return operand1 + operand2;
    }
}
```

Kita boleh membuat _test fixture_ seperti ini untuk mengujinya:

```csharp
using NUnit.Framework

[TestFixture]
public class CalculatorTest
{
    [Test]
    public void AddShouldDoSum()
    {
        var calc = new Calculator();
        var result = calc.Add(2, 1);

        Assert.AreEqual(3, result);
    }

    [Test]
    public void MinusShouldDoSubtraction()
    {
        var calc = new Calculator();
        var result = calc.Minus(2, 1);

        Assert.AreEqual(1, result);
    }
}
```

Setelah _test code_ di atas dikompil menjadi _assembly_ (DLL) atau _executable_, larikan ia menggunakan sama ada _console runner_ (nunit-console.exe) atau _GUI runner_ (nunit-gui.exe).

Di bawah adalah contoh apa bila ia dilarikan menggunakan _GUI NUnit runner_. Kita dapat lihat bahawa _test_ untuk fungsi _Add()_ berjaya, tetapi _test_ untuk _Minus()_ gagal kerana terdapat kesilapan dalam _code_ kita.

![Contoh antaramuka NUnit GUI Runner](http://i.imgur.com/m8z2n.png)

### Unit Test Python
Kod untuk testing dalam Python boleh ditulis dengan bantuan module `unittest` dalam Python Standard Library. Katakan kod yang ingin diuji adalah seperti berikut:

```python
class Calculator(object):
    def add(self, num1, num2):
        return num1 + num2

    def minus(self, num1, num2):
        return num1 + num2
```

Simpan kod di atas dalam fail bernama `calculator.py`. Seterusnya kod untuk testing boleh ditulis seperti berikut:-

```python
import unittest

from calculator import Calculator
        
class CalculatorTest(unittest.TestCase):
    def test_add_should_do_sum(self):
        calc = Calculator()
        result = calc.add(2, 1)

        self.assertEqual(result, 3)

    def test_minus_should_do_substraction(self):
        calc = Calculator()
        result = calc.minus(2, 1)

        self.assertEqual(result, 1)
        
if __name__ == '__main__':
    unittest.main()
```
Simpan kod di atas dalam fail bernama `tests.py`. Seterusnya kita boleh jalankan test dengan melancarkan arahan berikut melalui console:-

```console
python tests.py
```
Anda akan dapati outputnya seperti berikut:-

```console
.F
======================================================================
FAIL: test_minus_should_do_substraction (__main__.CalculatorTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "tests.py", line 16, in test_minus_should_do_substraction
    self.assertEqual(result, 1)
AssertionError: 3 != 1

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```
Di atas kita dapati satu test gagal kerana terdapat kesilapan dalam kod kita sebelum ini. Setelah kesilapan itu dibetulkan, kita akan dapati outputnya seperti berikut:-

```console
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

## Soalan Lazim
### Apa itu _assert_ ?
_Assertion_ merupakan satu proses menguji nilai pada bahagian-bahagian tertentu aturcara bagi memastikan ia sentiasa benar sebagaimana yang diharapkan oleh pengaturcara. Kegagalan pada _assertion_ boleh dianggap sebagai kegagalan langsung aturcara tersebut dan ia mesti dibetulkan. Ini berbeza dengan _error handling_ dimana ia sesuatu yang dijangka akan berlaku dan pengaturcara hanya perlu memastikan langkah-langkah sepatutnya dilakukan untuk menangani _error_ tersebut.[^1]

## Penulis
Nama-nama di bawah adalah penyumbang kepada tulisan ini:-

* Mohd. Kamal bin Mustafa (k4ml) - http://k4ml.github.com/
* Mohd Amree (amree) - http://ieatbinary.com/
* Mior Muhammad Zaki (crynobone) - http://crynobone.com/
* Irwan Azam Ahmad (ryzam) - https://github.com/ryzam
* Ikhwan Hayat (ikhwanhayat) - https://github.com/ikhwanhayat

[^1]: http://en.wikipedia.org/wiki/Assertion_(computing)
