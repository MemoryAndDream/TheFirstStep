# -*- mode: python -*-

block_cipher = None


a = Analysis(['D:\\pyproject\\doc_parser.py'],
             pathex=['D:\\pyproject', 'D:\\\xd3\xc3\xbb\xa7\xc4\xbf\xc2\xbc\\\xce\xd2\xb5\xc4\xce\xc4\xb5\xb5\\GitHub\\THEFIR~1\\WORD_P~1'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='doc_parser',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
