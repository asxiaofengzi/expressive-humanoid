import sys

# 添加路径
sys.path.append('/home/js/xiaofengzi/fbx/fbx_python_binding/build/Distrib/site-packages/fbx/')

# 打印 sys.path 以检查路径是否已添加
print(sys.path)

# 尝试导入一个模块来测试路径是否有效
try:
    import fbxsip  # 替换为你期望导入的模块名
    print("fbxsip Module imported successfully.")
except ImportError as e:
    print("Failed to import module:", e)