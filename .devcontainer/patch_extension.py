import sys
path = "/home/codespace/.vscode-remote/extensions/huff-language.huff-language-0.0.32/out/main.js"

try:
    with open(path, "r") as f:
        content = f.read()
except:
    print("ERROR: main.js no encontrado")
    sys.exit(1)

fixes = [
    ('hevm exec --code ${t.toString().replace("Return: ", "").trim()} --address ${e.hevmContractAddress} --create --caller ${e.hevmCaller} --gas 0xffffffff ${e.stateChecked||e.storageChecked?"--root "+i:""}', 'hevm exec --code ${t.toString().replace("Return: ", "").trim()} --address ${e.hevmContractAddress} --caller ${e.hevmCaller} --gas 0xffffffff'),
    ('hevm exec     --code ${e.toString()}     --address ${a}     --caller ${f}     --gas 0xffffffff     ${n||M?"--root "+(r.mountedDrive?"/mnt/"+C:"")+i+"/"+p:""}     ${b?"--calldata "+bp(v):""}     ${k?"--value "+T:""}     --debug', 'hevm exec --code ${e.toString()} --address ${a} --caller ${f} --gas 0xffffffff ${b?"--calldata "+bp(v):""} ${k?"--value "+T:""}'),
    ('hevm exec   --code ${t.toString().replace("Return: ", "").trim()}   --address ${i.hevmContractAddress}   --caller ${i.hevmCaller}   --gas 0xffffffff   --root ${(i.mountedDrive?"/mnt/"+i.mountedDrive:"")+n+"/"+i.statePath}   --debug   ${i.callValueChecked?"--value "+i.callValue:""}   ${e?"--calldata "+e:""}', 'hevm exec --code ${t.toString().replace("Return: ", "").trim()} --address ${i.hevmContractAddress} --caller ${i.hevmCaller} --gas 0xffffffff ${i.callValueChecked?"--value "+i.callValue:""} ${e?"--calldata "+e:""} --debug'),
    ('hevmContractAddress:cp("keccak256").update(Buffer.from(i.toString())).digest("hex").toString("hex").slice(0,42)', 'hevmContractAddress:"0x"+cp("keccak256").update(Buffer.from(i.toString())).digest("hex").toString("hex").slice(0,40)'),
    ('hevmContractAddress:D_("keccak256").update(Buffer.from(e)).digest("hex").toString("hex").slice(0,42)', 'hevmContractAddress:"0x"+D_("keccak256").update(Buffer.from(e)).digest("hex").toString("hex").slice(0,40)'),
    ('hevmCaller:"0x00000000000000000000000000000000000000420"', 'hevmCaller:"0x0000000000000000000000000000000000000420"'),
    ('huffc ${e} --bytecode', 'huffc --evm-version paris ${e} --bytecode'),
]

total = 0
for old, new in fixes:
    count = content.count(old)
    total += count
    content = content.replace(old, new)

with open(path, "w") as f:
    f.write(content)

print(f"Patches aplicados: {total}/7 ✓")
