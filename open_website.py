#!/usr/bin/env python3
"""
简单的Python脚本来在浏览器中打开网站进行检查
"""

import webbrowser
import os
import http.server
import socketserver
import threading
import time

def open_in_browser():
    """在默认浏览器中打开网站"""
    # 获取当前目录下的index.html文件路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_file = os.path.join(current_dir, 'index.html')
    
    # 检查文件是否存在
    if os.path.exists(html_file):
        # 使用file:// 协议直接打开
        file_url = f"file://{html_file}"
        print(f"在浏览器中打开: {file_url}")
        webbrowser.open(file_url)
        return True
    else:
        print(f"错误: 找不到文件 {html_file}")
        return False

def start_local_server(port=8000):
    """启动本地HTTP服务器"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_dir)
    
    handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            print(f"在端口 {port} 启动本地服务器...")
            print(f"访问: http://localhost:{port}")
            
            # 在新线程中启动服务器
            def serve():
                httpd.serve_forever()
            
            server_thread = threading.Thread(target=serve)
            server_thread.daemon = True
            server_thread.start()
            
            # 等待一秒钟让服务器启动
            time.sleep(1)
            
            # 在浏览器中打开
            webbrowser.open(f"http://localhost:{port}")
            
            print("按 Ctrl+C 停止服务器...")
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\n正在停止服务器...")
                
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"端口 {port} 已被占用，尝试端口 {port+1}")
            start_local_server(port+1)
        else:
            print(f"启动服务器时出错: {e}")

def main():
    """主函数"""
    print("=== 网站检查工具 ===")
    print("1. 直接在浏览器中打开 (file://)")
    print("2. 启动本地服务器 (推荐)")
    
    choice = input("请选择 (1/2, 默认2): ").strip()
    
    if choice == "1":
        open_in_browser()
    else:
        start_local_server()

if __name__ == "__main__":
    main()