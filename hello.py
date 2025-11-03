#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(description='Hello from CI Package Manager!')
    parser.add_argument('--name', default='World', help='Name to greet')
    parser.add_argument('--repeat', type=int, default=1, help='Number of times to repeat')
    
    args = parser.parse_args()
    
    for i in range(args.repeat):
        print(f"Hello {args.name}! 👋 (from CI Package #{i+1})")
    
    print(f"\n🎉 Package 'hello-ci' is working correctly!")
    print("💡 Try: hello.py --name YourName --repeat 3")

if __name__ == "__main__":
    main()
