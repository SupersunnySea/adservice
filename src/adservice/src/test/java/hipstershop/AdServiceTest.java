package hipstershop;

import com.google.common.collect.ImmutableListMultimap;
import io.grpc.ServerBuilder;
import org.junit.Before;
import org.junit.Test;

import java.io.IOException;
import java.security.PublicKey;
import java.util.*;

import static hipstershop.AdService.createAdsMap;
import static org.junit.Assert.*;

public class AdServiceTest {
    private AdService adservice;

    @Before
    public void setUp() throws Exception{
        adservice = AdService.getInstance();
    }

    @Test
    public void testgetAdsByCategory() throws Exception{
        String category = "photography";
        hipstershop.Demo.Ad camera =
                hipstershop.Demo.Ad.newBuilder()
                        .setRedirectUrl("/product/2ZYFJ3GM2N")
                        .setText("Film camera for sale. 80% off.")
                        .build();
        hipstershop.Demo.Ad lens =
                hipstershop.Demo.Ad.newBuilder()
                        .setRedirectUrl("/product/66VCHSJNUP")
                        .setText("Vintage camera lens for sale. 60% off.")
                        .build();
        Collection<hipstershop.Demo.Ad> collection=new Collection<hipstershop.Demo.Ad>() {
            @Override
            public int size() {
                return 0;
            }

            @Override
            public boolean isEmpty() {
                return false;
            }

            @Override
            public boolean contains(Object o) {
                return false;
            }

            @Override
            public Iterator<hipstershop.Demo.Ad> iterator() {
                return null;
            }

            @Override
            public Object[] toArray() {
                return new Object[0];
            }

            @Override
            public <T> T[] toArray(T[] a) {
                return null;
            }

            @Override
            public boolean add(hipstershop.Demo.Ad ad) {
                return false;
            }

            @Override
            public boolean remove(Object o) {
                return false;
            }

            @Override
            public boolean containsAll(Collection<?> c) {
                return false;
            }

            @Override
            public boolean addAll(Collection<? extends hipstershop.Demo.Ad> c) {
                return false;
            }

            @Override
            public boolean removeAll(Collection<?> c) {
                return false;
            }

            @Override
            public boolean retainAll(Collection<?> c) {
                return false;
            }

            @Override
            public void clear() {

            }
        };
        collection.add(camera);
        collection.add(lens);

        assertTrue(adservice.getAdsByCategory(category).contains(camera));
        assertTrue(adservice.getAdsByCategory(category).contains(lens));
        assertEquals(2,adservice.getAdsByCategory(category).size());
    }

    @Test
    public void testGetRandomAds(){
        List<hipstershop.Demo.Ad> list = null;
        assertNull(list);
        list = adservice.getRandomAds();
        assertNotNull(list);
        assertEquals(2,list.size());
    }

//    @Test
//    public void testStop(){
//        try{
//            adservice.server =
//                    ServerBuilder.forPort(9555)
//                            .addService(new AdService.AdServiceImpl())
//                            .addService(adservice.healthMgr.getHealthService())
//                            .build()
//                            .start();
//        }catch (IOException e){
//            e.printStackTrace();
//        }
//
//        adservice.stop();
//        assertEquals(server,);
//    }

    @Test
    public void testCreateAdsMap() {
        hipstershop.Demo.Ad camera =
                hipstershop.Demo.Ad.newBuilder()
                        .setRedirectUrl("/product/2ZYFJ3GM2N")
                        .setText("Film camera for sale. 80% off.")
                        .build();
        hipstershop.Demo.Ad lens =
                hipstershop.Demo.Ad.newBuilder()
                        .setRedirectUrl("/product/66VCHSJNUP")
                        .setText("Vintage camera lens for sale. 60% off.")
                        .build();
        hipstershop.Demo.Ad recordPlayer =
                hipstershop.Demo.Ad.newBuilder()
                        .setRedirectUrl("/product/0PUK6V6EV0")
                        .setText("Vintage record player for sale. 30% off.")
                        .build();
        hipstershop.Demo.Ad bike =
                hipstershop.Demo.Ad.newBuilder()
                        .setRedirectUrl("/product/9SIQT8TOJO")
                        .setText("City Bike for sale. 10% off.")
                        .build();
        hipstershop.Demo.Ad baristaKit =
                hipstershop.Demo.Ad.newBuilder()
                        .setRedirectUrl("/product/1YMWWN1N4O")
                        .setText("Home Barista kitchen kit for sale. Buy one, get second kit for free")
                        .build();
        hipstershop.Demo.Ad airPlant =
                hipstershop.Demo.Ad.newBuilder()
                        .setRedirectUrl("/product/6E92ZMYYFZ")
                        .setText("Air plants for sale. Buy two, get third one for free")
                        .build();
        hipstershop.Demo.Ad terrarium =
                hipstershop.Demo.Ad.newBuilder()
                        .setRedirectUrl("/product/L9ECAV7KIM")
                        .setText("Terrarium for sale. Buy one, get second one for free")
                        .build();
        ImmutableListMultimap<String, hipstershop.Demo.Ad> listMultimap = adservice.createAdsMap();
        assertTrue(listMultimap.containsEntry("photography",camera));
        assertTrue(listMultimap.containsEntry("photography",lens));
        assertTrue(listMultimap.containsEntry("vintage",camera));
        assertTrue(listMultimap.containsEntry("vintage",lens));
        assertTrue(listMultimap.containsEntry("vintage",recordPlayer));
        assertTrue(listMultimap.containsEntry("cycling",bike));
        assertTrue(listMultimap.containsEntry("cookware",baristaKit));
        assertTrue(listMultimap.containsEntry("gardening",airPlant));
        assertTrue(listMultimap.containsEntry("gardening",terrarium));

    }



}
