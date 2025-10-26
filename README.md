# gfw
<code>openssl x509 -in AnyHotmailCom_201501.crt -text -noout</code><br>
<code>TEWA-708G Tianyi_V1.0.3 mtd11.bin rootfs_ubifs</code><br>
<code>unsquashfs -d ./TWWA-708G mtd11.bin</code><br>
<code>Or</code>
<code>mtd0.bin rootfs</code><br>
<code>pip3 install ubi_reader</code><br>
<code>ubireader_extract_images mtd0.bin</code><br>
<code>unsquashfs -d ./TWWA-708G ubifs-root/mtd0.bin/img-860373306_vol-rootfs_ubifs.ubifs</code>
