import {Router,Request,Response} from 'express';
import { getRepository } from 'typeorm';
import {Master} from '../models/Master'
import { createQueryBuilder } from 'typeorm';
import { getManager } from 'typeorm';

const router =  Router();



router.get('/', async (req: Request, resp:Response) => {
  const manager = getManager();
  const rawData = await manager.query(`SELECT username
  from master m join details d on (m.id = d.idId)  
  where d.postal_code =`+req.query.id);
    resp.json(rawData);

  })

router.delete('/',async (req: Request, resp:Response) => {
    const manager = getManager();
    const rawData = await manager.query(`DELETE FROM master WHERE id  IN (SELECT idid from details where postal_code==`+req.query.id+")");
  
    const rawData2 = manager.query("DELETE FROM details   where details.postal_code="+req.query.id);
    resp.json(rawData);
    
  })

export default router;