#coding=utf-8

from Cryptodome.Cipher import AES
from Cryptodome import Random
from binascii import b2a_hex
from binascii import a2b_hex

class AESUtil:

    """
        密匙key，必须为16(AES-128)、24位(AES-192)、32位(AES-256)bytes长度
    """
    #目前16位够用
    key = b"#5TRuc*MH78I!Lc@"

    #生成长度等于AES块大小的不可重复的密匙向量
    iv = Random.new().read(AES.block_size)

    @classmethod
    def encrypt(cls, data):
        # 使用key和iv初始化AES对象
        mycipher = AES.new(cls.key, AES.MODE_CFB, cls.iv)
        return b2a_hex(cls.iv+mycipher.encrypt(data.encode())).decode()

    @classmethod
    def decrypt(cls, m_str):
        mm = a2b_hex(m_str)
        mydecrypt = AES.new(cls.key, AES.MODE_CFB, mm[:16])
        return mydecrypt.decrypt(mm[16:]).decode()

if __name__ == '__main__':
    print(AESUtil.encrypt("111111"))

