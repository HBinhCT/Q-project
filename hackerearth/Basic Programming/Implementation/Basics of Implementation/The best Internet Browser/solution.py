vowels = "aeiou"
tc = int(input())
for _ in range(tc):
    website_name = input().strip()
    parts = website_name.split(".")
    new_sld = "".join(i for i in parts[1] if i not in vowels)
    new_domain = new_sld + "." + parts[-1]
    print(f"{len(new_domain)}/{len(website_name)}")
