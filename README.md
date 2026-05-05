<div align="center">
  <h1>UTS Kriptoanalisis</h1>
  <p><i>Daftar Soal</i></p>
</div>

<hr>

<h2>Soal 1: Kriptografi Modern <code>(35 poin)</code></h2>

<ul>
  <li><b>Buat program (Python/pseudocode) untuk:</b>
    <ul>
      <li>Enkripsi menggunakan XOR</li>
      <li>Dekripsi menggunakan XOR</li>
    </ul>
  </li>
  <li><b>Gunakan input:</b>
    <ul>
      <li>Plainteks: bebas (minimal 16 bit / 2 karakter)</li>
      <li>Kunci: bebas</li>
    </ul>
  </li>
  <li><b>Lakukan eksperimen:</b>
    <ul>
      <li>Kunci pendek (berulang)</li>
      <li>Kunci acak (panjang sama dengan plainteks)</li>
    </ul>
  </li>
</ul>

<h4>Pertanyaan Analisis:</h4>
<ul>
  <li>Apa yang terjadi jika kunci diulang?</li>
  <li>Mengapa XOR cipher sederhana tidak aman?</li>
  <li>Kapan XOR menjadi sangat aman?</li>
</ul>

<h4>Output yang diharapkan:</h4>
<ul>
  <li>Kode program</li>
  <li>Screenshot hasil</li>
</ul>

<br><hr>

<h2>Soal 2: Membandingkan Algoritma Klasik dan Modern</h2>

<p><b>Implementasikan:</b></p>
<ul>
  <li>Caesar Cipher (klasik)</li>
  <li>XOR Cipher / Stream Cipher sederhana (modern)</li>
  <li><i>Gunakan plainteks yang sama untuk keduanya.</i></li>
</ul>

<p><b>Bandingkan hasil:</b></p>
<ul>
  <li>Cipherteks</li>
  <li>Kompleksitas</li>
  <li>Keamanan</li>
</ul>

<h4>Pertanyaan Analisis:</h4>
<ul>
  <li>Mengapa kriptografi klasik mudah dipecahkan?</li>
  <li>Apa kelebihan kriptografi modern?</li>
  <li>Bagaimana peran komputer dalam kriptografi modern?</li>
</ul>

<h4>Output yang diharapkan:</h4>
<ul>
  <li>Kode program</li>
  <li>Tabel perbandingan</li>
  <li>Analisis</li>
</ul>

<br><hr>

<h2>Soal 3: Simulasi Serangan & Kelemahan Cipher <code>(30 poin)</code></h2>

<p><b>Diberikan kondisi berikut:</b></p>
<ul>
  <li>Cipher menggunakan XOR dengan kunci berulang.</li>
  <li>Sebagian plainteks diketahui (<i>known plaintext</i>).</li>
</ul>

<ol>
  <li><b>Buat simulasi:</b>
    <ul>
      <li>Enkripsi pesan menggunakan XOR dengan kunci pendek.</li>
      <li>Asumsikan <i>attacker</i> mengetahui sebagian plainteks.</li>
    </ul>
  </li>
  <li><b>Tunjukkan bagaimana:</b>
    <ul>
      <li>Kunci dapat ditebak.</li>
      <li>Pesan lain dapat dibuka.</li>
    </ul>
  </li>
</ol>

<h4>Pertanyaan Analisis:</h4>
<ul>
  <li>Mengapa <i>keystream</i> berulang berbahaya?</li>
  <li>Bandingkan dengan:
    <ul>
      <li><i>Keystream</i> nol</li>
      <li><i>Keystream</i> acak</li>
    </ul>
  </li>
</ul>

<h4>Output yang diharapkan:</h4>
<ul>
  <li>Kode simulasi</li>
  <li>Penjelasan proses serangan</li>
  <li>Kesimpulan keamanan</li>
</ul>


