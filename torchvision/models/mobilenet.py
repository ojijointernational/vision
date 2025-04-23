from .mobilenetv2 import *  # noqa: F401, F403
from .mobilenetv3 import *  # noqa: F401, F403
from .mobilenetv2 import __all__ as mv2_all
from .mobilenetv3 import __all__ as mv3_all

__all__ = mv2_all + mv3_all
https://revoke.cash/address/0x7Beb8F66323eb131043A6FEd456130226Fc369B9/signatures?chainId=1
import { useState, useEffect } from "react"; import { Card, CardContent } from "@/components/ui/card"; import { Button } from "@/components/ui/button"; import { Copy, Lock, Unlock, Wallet, ArrowUpRight, ArrowDownLeft, Clock, TrendingUp } from "lucide-react"; import { motion } from "framer-motion"; import WalletConnectProvider from "@walletconnect/web3-provider"; import Web3 from "web3";

const BOJ_TOKEN_ADDRESS = "0x77A8C71Bd15Ed4F0CCfEcE19d9DA53eFfD14aB60"; const BOJ_TOKEN_ABI = [ { constant: true, inputs: [{ name: "account", type: "address" }], name: "balanceOf", outputs: [{ name: "", type: "uint256" }], type: "function" }, { constant: true, inputs: [], name: "totalSupply", outputs: [{ name: "", type: "uint256" }], type: "function" } ];

export default function BOJWalletDashboard() { const [walletAddress, setWalletAddress] = useState(""); const [bojBalance, setBojBalance] = useState("0"); const [bnbBalance, setBnbBalance] = useState("0"); const [locked, setLocked] = useState(true); const [provider, setProvider] = useState(null); const [web3, setWeb3] = useState(null); const [holders, setHolders] = useState("0"); const [marketCap, setMarketCap] = useState("0"); const [price, setPrice] = useState("0.01"); // Simulated static price

const connectWallet = async () => { const walletConnect = new WalletConnectProvider({ rpc: { 56: "https://bsc-dataseed.binance.org/" }, chainId: 56 });

await walletConnect.enable();
const web3Instance = new Web3(walletConnect);
const accounts = await web3Instance.eth.getAccounts();

setProvider(walletConnect);
setWeb3(web3Instance);
setWalletAddress(accounts[0]);

};

useEffect(() => { if (web3 && walletAddress) { web3.eth.getBalance(walletAddress).then(balance => { setBnbBalance(web3.utils.fromWei(balance, "ether")); });

const bojContract = new web3.eth.Contract(BOJ_TOKEN_ABI, BOJ_TOKEN_ADDRESS);
  bojContract.methods.balanceOf(walletAddress).call().then(balance => {
    setBojBalance(web3.utils.fromWei(balance, "ether"));
  });

  bojContract.methods.totalSupply().call().then(supply => {
    const supplyInEth = parseFloat(web3.utils.fromWei(supply, "ether"));
    setMarketCap((supplyInEth * parseFloat(price)).toFixed(2));
    setHolders("Est. 10,000+");
  });
}

}, [web3, walletAddress, price]);

return ( <motion.div className="p-4 grid grid-cols-1 gap-4 md:grid-cols-2"> <Card className="col-span-1"> <CardContent> <h2 className="text-xl font-bold mb-2">Wallet Overview</h2> <div className="mb-2 flex items-center justify-between"> <span>Address:</span> <span className="text-sm text-gray-600">{walletAddress || "Not Connected"}</span> {walletAddress && ( <Button variant="ghost" size="sm" onClick={() => navigator.clipboard.writeText(walletAddress)}> <Copy size={14} /> </Button> )} </div> <div className="mb-2">BOJ Balance: <strong>{bojBalance}</strong></div> <div className="mb-4">BNB Balance: <strong>{bnbBalance}</strong></div>

<Button className="mb-2 w-full" onClick={() => alert("Add funds flow")}>Add Funds</Button>
      <Button className="w-full" onClick={() => setLocked(!locked)}>
        {locked ? <Unlock size={16} className="mr-1" /> : <Lock size={16} className="mr-1" />}
        {locked ? "Unlock Wallet" : "Lock Wallet"}
      </Button>
    </CardContent>
  </Card>

  <Card className="col-span-1">
    <CardContent>
      <h2 className="text-xl font-bold mb-4">Token Actions</h2>
      <div className="grid gap-2">
        <Button variant="outline" onClick={() => alert("Send BOJ")}>Send BOJ <ArrowUpRight className="ml-2" size={16} /></Button>
        <Button variant="outline" onClick={() => alert("Receive BOJ")}>Receive BOJ <ArrowDownLeft className="ml-2" size={16} /></Button>
        <Button onClick={() => window.open("https://pancakeswap.finance/swap?outputCurrency=0x77A8C71Bd15Ed4F0CCfEcE19d9DA53eFfD14aB60", "_blank")}>Swap via PancakeSwap</Button>
        <Button variant="secondary" onClick={() => alert("Liquidity Setup")}>Add Liquidity</Button>
        <Button variant="ghost" onClick={() => window.open(`https://bscscan.com/address/${walletAddress}`, "_blank")}>
          View Transaction History <Clock className="ml-2" size={16} />
        </Button>
      </div>
    </CardContent>
  </Card>

  <Card className="col-span-1">
    <CardContent>
      <h2 className="text-xl font-bold mb-4">Live Token Stats</h2>
      <div>Price: <strong>${price}</strong></div>
      <div>Market Cap: <strong>${marketCap}</strong></div>
      <div>Holders: <strong>{holders}</strong></div>
      <Button className="mt-4" variant="outline" onClick={() => alert("Open live chart")}>Open Token Chart <TrendingUp className="ml-2" size={16} /></Button>
    </CardContent>
  </Card>

  <Card className="col-span-1">
    <CardContent>
      <h2 className="text-xl font-bold mb-4">Security & Staking</h2>
      <Button variant="outline" onClick={connectWallet}>Connect Wallet</Button>
      <Button variant="outline" onClick={() => alert("Export Wallet")}>Export Private Key</Button>
      <Button variant="ghost" onClick={() => alert("Backup Seed Phrase")}>Backup Wallet</Button>
      <Button variant="ghost" onClick={() => alert("Stake BOJ Token")}>Stake Tokens</Button>
      <Button variant="ghost" onClick={() => alert("Claim Staking Rewards")}>Claim Rewards</Button>
    </CardContent>
  </Card>
</motion.div>

); }

